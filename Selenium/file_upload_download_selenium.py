"""
file_upload_download.py
=========================
Selenium examples: handling file upload and file download.
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ============================================================
# 1. FILE UPLOAD — standard <input type="file">
# ============================================================
"""
Most upload widgets are just an <input type="file"> element, even if
it's visually hidden (e.g. a custom "Choose File" button covers it via
CSS). Selenium can interact with it directly WITHOUT touching the
native OS file-picker dialog, which Selenium cannot control anyway
(it's outside the browser's DOM).

Key rule: use the ABSOLUTE file path with send_keys().
"""

def upload_file_basic(driver, file_input_locator, file_path):
    """
    Standard upload — works when <input type="file"> is present in DOM,
    even if display:none / visibility:hidden via CSS.
    """
    file_path = os.path.abspath(file_path)   # always use absolute path
    file_input = driver.find_element(*file_input_locator)
    file_input.send_keys(file_path)


# Example usage against the-internet.herokuapp.com/upload (public demo site)
def demo_upload():
    driver = webdriver.Chrome()
    try:
        driver.get("https://the-internet.herokuapp.com/upload")

        FILE_INPUT = (By.ID, "file-upload")
        UPLOAD_BUTTON = (By.ID, "file-submit")
        UPLOADED_FILENAME = (By.ID, "uploaded-files")

        # create a dummy file to upload
        dummy_path = os.path.join(os.getcwd(), "sample_upload.txt")
        with open(dummy_path, "w") as f:
            f.write("Hello Selenium upload test")

        upload_file_basic(driver, FILE_INPUT, dummy_path)
        driver.find_element(*UPLOAD_BUTTON).click()

        result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(UPLOADED_FILENAME)
        )
        print("Uploaded file name shown on page:", result.text)
        assert result.text == "sample_upload.txt"

    finally:
        driver.quit()


# ============================================================
# 2. FILE UPLOAD — hidden input with NO visible <input> at all
#    (custom drag-and-drop widgets, React/Angular components)
# ============================================================
"""
Some frameworks render the <input type="file"> completely hidden
(e.g. opacity:0, height:0) and only show a styled "drop zone" div.
send_keys() still works AS LONG AS the input tag genuinely exists in
the DOM. If it truly doesn't render an <input> at all (rare, drag-drop
only via JS DataTransfer), you may need to unhide it via JS first:
"""

def upload_file_forced_visible(driver, file_input_locator, file_path):
    file_path = os.path.abspath(file_path)
    file_input = driver.find_element(*file_input_locator)

    # Force it to be interactable if some frameworks block send_keys
    # on a 0x0 / display:none element
    driver.execute_script(
        "arguments[0].style.display='block'; "
        "arguments[0].style.visibility='visible'; "
        "arguments[0].style.opacity='1'; "
        "arguments[0].style.height='auto'; "
        "arguments[0].style.width='auto';",
        file_input,
    )
    file_input.send_keys(file_path)


# ============================================================
# 3. UPLOADING MULTIPLE FILES
# ============================================================
"""
If the input has the `multiple` attribute, pass multiple paths
separated by a newline character "\\n" in a single send_keys() call.
"""

def upload_multiple_files(driver, file_input_locator, file_paths):
    joined_paths = "\n".join(os.path.abspath(p) for p in file_paths)
    driver.find_element(*file_input_locator).send_keys(joined_paths)


# ============================================================
# 4. FILE DOWNLOAD — configuring Chrome to auto-download without a
#    "Save As" dialog, then verifying the file landed on disk
# ============================================================
"""
Selenium cannot interact with OS-level "Save As" dialogs (they're
outside the browser process). The standard approach is to configure
the browser BEFORE launching it to auto-download files to a known
folder, skipping the dialog entirely — then verify the file exists
in that folder afterward.
"""

def get_chrome_driver_with_download_dir(download_dir):
    """Configures Chrome to silently download files to `download_dir`
    with no 'Save As' prompt."""
    download_dir = os.path.abspath(download_dir)
    os.makedirs(download_dir, exist_ok=True)

    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_dir,   # target folder
        "download.prompt_for_download": False,          # skip Save As dialog
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,                   # avoid "keep/discard" warnings
    }
    options.add_experimental_option("prefs", prefs)
    return webdriver.Chrome(options=options)


def wait_for_download_complete(download_dir, timeout=30):
    """
    Polls the download folder until a finished file appears.
    Chrome names in-progress downloads with a '.crdownload' extension,
    so we wait until no such temp file remains AND at least one real
    file exists.
    """
    seconds = 0
    while seconds < timeout:
        files = os.listdir(download_dir)
        if files and not any(f.endswith(".crdownload") for f in files):
            return files
        time.sleep(1)
        seconds += 1
    raise TimeoutError(f"Download did not complete within {timeout}s")


# Example usage: download a PDF/file from a link and verify it saved
def demo_download():
    download_dir = os.path.join(os.getcwd(), "downloads")
    driver = get_chrome_driver_with_download_dir(download_dir)
    try:
        driver.get("https://the-internet.herokuapp.com/download")

        # Click the first available download link on the demo page
        first_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href$='.txt'], a[href$='.jpg']"))
        )
        first_link.click()

        downloaded_files = wait_for_download_complete(download_dir)
        print("Downloaded files:", downloaded_files)
        assert len(downloaded_files) > 0

    finally:
        driver.quit()


# ============================================================
# 5. POM-STYLE WRAPPER (fits the BasePage pattern used elsewhere)
# ============================================================
"""
In a real POM framework, upload/download logic usually lives on
BasePage so any page object can call self.upload_file(...) or
self.download_and_verify(...).
"""

class BasePageFileHelpers:
    """Mixin-style helpers — inherit alongside your normal BasePage."""

    def upload_file(self, locator, file_path):
        self.driver.find_element(*locator).send_keys(os.path.abspath(file_path))

    def download_and_verify(self, locator, download_dir, timeout=30):
        self.driver.find_element(*locator).click()
        return wait_for_download_complete(download_dir, timeout)


if __name__ == "__main__":
    demo_upload()
    demo_download()
