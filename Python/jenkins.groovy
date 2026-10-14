"""
==== Jenkins ====
Document: https://www.jenkins.io/doc/
Youtube reference:  https://www.youtube.com/watch?v=7KCS70sCoK0
Jenkins Environment variables list: https://devopsqa.wordpress.com/2019/11/19/list-of-available-jenkins-environment-variables/

"""

pipeline {
    agent any
    environment{
        NEW_VERSION = '6.6.2'
    }
    stages{
        stage("build"){
            steps{
                println "Building version ${NEW_VERSION}"
                script{
                    println "Build"
                }
            }
        }
        stage("test"){
            steps{
                script{
                println "Test"
                }
            }
        }
        stage("deploy"){
            steps{
                script{
                println "Deploy"
                }
            }
        }
    }
    post{
        // it's like finally block(Used to send emails about build)
        failure{
            // script to check build failures
        }
        success{
            // script to check build success
        }
    }
}
