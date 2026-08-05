from datasentinel.reports.html_report import HTMLReport
from datasentinel.reports.pdf_report import PDFReport
validation = [

    {
        "rule":"null_check",
        "column":"name",
        "passed":False,
        "violations":1
    },

    {
        "rule":"unique_check",
        "column":"id",
        "passed":False,
        "violations":1
    },

]

schema = {

    "added":["salary"],

    "removed":["age"],

    "changed":[]

}

anomaly = [

    {

        "method":"iqr",

        "column":"salary",

        "count":1

    }

]

report = HTMLReport()

path = report.generate(

    validation,

    schema,

    anomaly,

)
pdf = PDFReport.generate(
    validation,
    schema,
    anomaly,
)



print(pdf)
print(path)