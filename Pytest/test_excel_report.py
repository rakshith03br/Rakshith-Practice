import pytest
import openpyxl
import pytest_html
from openpyxl.drawing.image import Image

def get_names():
    return ['a','b','c','d','e']

class TestExcelReport:
    def test_generate_excel_sheet(self):
        # Call the function that returns the list of names
        names_list = get_names()

        # Create a new workbook and select the active sheet
        workbook = openpyxl.Workbook()
        sheet = workbook.active

        # Add headers
        sheet["A1"] = "Name"
        sheet["B1"] = "Result"
        sheet["C1"] = "Reason"

        for name in names_list:
            if len(name) <= 5:
                result = "Pass"
                reason = ""
            else:
                result = "Fail"
                reason = "Name is too long"

                # Append results to the sheet
            sheet.append([name, result, reason])
        # Save the workbook
        workbook.save("test_report.xlsx")
'''
for getting excel report in html report
##########on head##########
<style>
.excel-sheet {
    width: 100%;
    height: 500px;
}
</style>

#######on body###########
<h2>Excel Sheet</h2>
<iframe class="excel-sheet" src="test_report.xlsx"></iframe>
'''
