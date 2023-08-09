# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"S30..00","system":"readv2"},{"code":"S300.00","system":"readv2"},{"code":"S300200","system":"readv2"},{"code":"S300300","system":"readv2"},{"code":"S300311","system":"readv2"},{"code":"S300400","system":"readv2"},{"code":"S300600","system":"readv2"},{"code":"S300700","system":"readv2"},{"code":"S300800","system":"readv2"},{"code":"S300900","system":"readv2"},{"code":"S300y11","system":"readv2"},{"code":"S300z00","system":"readv2"},{"code":"S301.00","system":"readv2"},{"code":"S301311","system":"readv2"},{"code":"S301400","system":"readv2"},{"code":"S301600","system":"readv2"},{"code":"S301700","system":"readv2"},{"code":"S301800","system":"readv2"},{"code":"S301900","system":"readv2"},{"code":"S301y11","system":"readv2"},{"code":"S30y.00","system":"readv2"},{"code":"S30z.00","system":"readv2"},{"code":"SC03.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('fracture-of-hip-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["femursubcapital-fracture-of-hip---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["femursubcapital-fracture-of-hip---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["femursubcapital-fracture-of-hip---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
