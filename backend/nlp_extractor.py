import re


def extract_invoice_fields(text):

    lines = text.split("\n")
    clean_text = text.replace("\n", " ")

    result = {

        "invoice_number": "Not Found",
        "invoice_date": "Not Found",
        "due_date": "Not Found",
        "total_amount": "Not Found",
        "vendor_name": "Not Found",
        "customer_name": "Not Found",
        "gst_number": "Not Found",
        "phone": "Not Found"

    }


    # ---------------------
    # invoice number
    # ---------------------

    for i, line in enumerate(lines):

        if "invoice no" in line.lower():

            # try same line
            match = re.search(r'[A-Z]{2,}\d{4,}', line)

            if match:

                result["invoice_number"] = match.group()

            else:

                # try next line
                if i+1 < len(lines):

                    next_line = lines[i+1]

                    match = re.search(r'[A-Z]{2,}\d{4,}', next_line)

                    if match:
                        result["invoice_number"] = match.group()


    # fallback search anywhere
    if result["invoice_number"] == "Not Found":

        match = re.search(
            r'[A-Z]{2,}\d{4,}',
            clean_text
        )

        if match:

            result["invoice_number"] = match.group()


    # ---------------------
    # invoice date
    # ---------------------

    date_match = re.search(
        r'\d{2}-\d{2}-\d{4}',
        clean_text
    )

    if date_match:

        result["invoice_date"] = date_match.group()


    # ---------------------
    # due date
    # ---------------------

    for i, line in enumerate(lines):

        if "due date" in line.lower():

            match = re.search(
                r'\d{2}-\d{2}-\d{4}',
                line
            )

            if match:

                result["due_date"] = match.group()


    # ---------------------
    # total amount
    # ---------------------

    totals = re.findall(
        r'\d+\.\d{2}',
        clean_text
    )

    if totals:

        result["total_amount"] = totals[-1]


    # ---------------------
    # vendor name
    # ---------------------

    vendor = re.search(
        r'[A-Z ]+(PVT|PRIVATE|LTD|LIMITED|PHARMA|MEDICAL|TRADERS)',
        clean_text
    )

    if vendor:

        result["vendor_name"] = vendor.group()


    # ---------------------
    # customer name
    # ---------------------

    for i, line in enumerate(lines):

        if "party name" in line.lower():

            if i+1 < len(lines):

                name_line = lines[i+1].strip()

                name = name_line.split(",")[0]

                result["customer_name"] = name


    # ---------------------
    # gst
    # ---------------------

    gst = re.search(
        r'\d{2}[A-Z]{5}\d{4}[A-Z]{1}\d[Z]{1}\d',
        clean_text
    )

    if gst:

        result["gst_number"] = gst.group()


    # ---------------------
    # phone
    # ---------------------

    phone = re.search(
        r'[6-9]\d{9}',
        clean_text
    )

    if phone:

        result["phone"] = phone.group()


    return result