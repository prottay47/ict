import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 1. Read raw file
input_path = 'Durontoitexq.md'
with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
    raw_lines = f.readlines()

print(f"Total lines in {input_path}: {len(raw_lines)}")

# 2. Master Cleaning Function
def clean_duronto_lines(lines_slice):
    cleaned_lines = []
    in_picture_text = False
    
    for line in lines_slice:
        s = line.strip()
        
        # Check picture text blocks
        if '<!-- Start of picture text -->' in s:
            in_picture_text = True
            continue
        if '<!-- End of picture text -->' in s:
            in_picture_text = False
            continue
        if in_picture_text:
            continue
            
        # Check noise lines to drop entirely
        # Links and group promos
        if re.search(r'(?i)facebook\.com|duranta\.app|duranta\.ac', s):
            continue
        # Watermarks & Academy Branding
        if re.search(r'দরন.*ক.*যার|Duranta Career|SMART IT JOB SOLUTION|CSE CAREER MASTER GUIDE|Engr\.\s*Md\.\s*Manik\s*Uddin', s):
            continue
        # Running headers / duplicate watermark labels
        if s in [
            '**Question Solution** En', '**Question Solution**', 'Question Solution', 
            'Question Solution En', '**NWPGCL AM ICT 24**', '**Question Solution** <u>En</u>',
            'am)o ‘', 'am)o \'', '_______=Zf', 'ee |', '~~SS~~', '~~———~~', '~~ee~~',
            '**Question Bank AE/AP/AME**', 'Question Bank AE/AP/AME', 'NWPGCL JAM ICT - DUET'
        ]:
            continue
        if re.match(r'^[\|\s\\]*\*\*Question Solution\*\*.*', s):
            continue
        if re.match(r'^\s*`?দরন.*', s):
            continue
        if re.match(r'^\s*\[\d+\]\s*$', s):
            continue
        if re.match(r'^\s*(?:Officer|Senior Officer)\s*\(IT\)\s*ID-\d+\s*$', s):
            continue
        if re.match(r'^\s*\d{5}-\s*\d{1,2}\s*$', s):
            continue
            
        # Clean inline HTML & formatting artifacts
        line_clean = re.sub(r'~~<u>.*?</u>~~|~~.*?~~', '', line)
        line_clean = re.sub(r'<mark>(.*?)</mark>', r'\1', line_clean)
        line_clean = re.sub(r'<u>(.*?)</u>', r'\1', line_clean)
        line_clean = line_clean.replace('', '-')
        line_clean = re.sub(r'^(\s*)[•]\s*', r'\1- ', line_clean)
        
        cleaned_lines.append(line_clean)
        
    result = '\n'.join(cleaned_lines)
    result = re.sub(r'\n{3,}', '\n\n', result)
    return result.strip()

# 3. Master List of 60 Exam Modules & Papers
exam_rules = [
    # 01 Power Sector
    (r'West Zone Power Distribution Company Limited \(WZPDCL\)\s*Assistant Engineer \(CSE/CS/ECE/ETE\)',
     '01_Power_Sector', '01_WZPDCL_Assistant_Engineer_CSE_2023.md', 'WZPDCL - Assistant Engineer (CSE/CS/ECE/ETE) - 2023', 'WZPDCL', 'Assistant Engineer (CSE)', 'KUET', '27/05/2023', '100 Marks (30 Non + 70 Dept)'),

    (r'North West Power Generation Company Limited \(NWPGCL\)\s*Post: AM \(ICT\), Date: 12/01/2024',
     '01_Power_Sector', '02_NWPGCL_AM_ICT_2024.md', 'NWPGCL - Assistant Manager (ICT) - 2024', 'NWPGCL', 'Assistant Manager (ICT)', 'BUET', '12/01/2024', '100 Marks (60 Non + 40 Dept)'),

    (r'BR Power Generation Company Limited \(BRPL\)\s*Exam Date: 29\.03\.2024',
     '01_Power_Sector', '03_BR_Powergen_BRPL_AM_ICT_2024.md', 'BR Powergen (BRPL) - Assistant Manager (ICT) - 2024', 'BRPL', 'Assistant Manager (ICT)', 'BUET', '29/03/2024', '100 Marks'),

    (r'Dhaka Electric Supply Company Limited \(DESCO\) Post Name: Sub-Assistant Engineer',
     '01_Power_Sector', '04_DESCO_Sub_Assistant_Engineer_2022.md', 'DESCO - Sub-Assistant Engineer (ICT/Electrical) - 2022', 'DESCO', 'Sub-Assistant Engineer (ICT)', 'BUET', '2022', '100 Marks'),

    (r'West Zone Power Distribution Company Ltd \(WZPDCL\) Assistant Engineer \(CSE\), Date: 29-06-2019',
     '01_Power_Sector', '05_WZPDCL_Assistant_Engineer_CSE_2019.md', 'WZPDCL - Assistant Engineer (CSE) - 2019', 'WZPDCL', 'Assistant Engineer (CSE)', 'KUET', '29/06/2019', '100 Marks (30 Non + 70 Dept)'),

    (r'West Zone Power Distribution Company Limited \(WZPDCL\)-\s*2023 Post: Sub-Assistant Engineer',
     '01_Power_Sector', '06_WZPDCL_Sub_Assistant_Engineer_CSE_2023.md', 'WZPDCL - Sub-Assistant Engineer (CSE) - 2023', 'WZPDCL', 'Sub-Assistant Engineer (CSE)', 'KUET', '27/05/2023', '100 Marks'),

    (r'Dhaka Electric Supply Company Ltd\.-2022.*Post: Assistant Engineer-IT',
     '01_Power_Sector', '07_DESCO_Assistant_Engineer_IT_2022.md', 'DESCO - Assistant Engineer (IT) - 2022', 'DESCO', 'Assistant Engineer (IT)', 'BUET', '19/11/2022', '100 Marks'),

    (r'Dhaka Electricity Supply PLC \(DESCO\) Exam Date: 15/05/2026 Post: Sub-Assistant',
     '01_Power_Sector', '08_DESCO_Sub_Assistant_Engineer_2026.md', 'DESCO - Sub-Assistant Engineer - 2026', 'DESCO', 'Sub-Assistant Engineer', 'BUET', '15/05/2026', '100 Marks'),

    (r'Nuclear Power Plant Company Bangladesh limited Post: Engineer \(Cyber Security Analyst\)',
     '01_Power_Sector', '09_NPCBL_Engineer_Cyber_Security_Analyst_2024.md', 'NPCBL - Engineer (Cyber Security Analyst) - 2024', 'NPCBL', 'Engineer (Cyber Security Analyst)', 'DUET/MIST', '2024', '100 Marks'),

    # 02 Bank IT
    (r'Bangladesh Bank Assistant programmer 2023 Exam Taker: BIBM',
     '02_Bank_IT', '01_Bangladesh_Bank_Assistant_Programmer_2023.md', 'Bangladesh Bank - Assistant Programmer - 2023', 'Bangladesh Bank', 'Assistant Programmer', 'BIBM', '03/02/2023', '200 Marks'),

    (r'Bangladesh Bank Assistant Maintenance Engineer 04\.02\.2023',
     '02_Bank_IT', '02_Bangladesh_Bank_Assistant_Maintenance_Engineer_2023.md', 'Bangladesh Bank - Assistant Maintenance Engineer (AME) - 2023', 'Bangladesh Bank', 'Assistant Maintenance Engineer', 'BIBM', '04/02/2023', '200 Marks'),

    (r'Bangladesh Bank Banker’s Selection Committee Secretariate \(BSCS\) Assistant Engineer \(IT\)',
     '02_Bank_IT', '03_Bangladesh_Bank_BSCS_AE_IT_AME_2024.md', 'Bangladesh Bank BSCS - Assistant Engineer (IT) / AME - 2024', 'Bangladesh Bank BSCS', 'Assistant Engineer (IT) / AME', 'BSCS/BIBM', '2024', '200 Marks'),

    (r'Combined 5 Bank Date: 03\.02\.2023 Exam taker: BIBM',
     '02_Bank_IT', '04_Combined_5_Bank_Officer_IT_2023.md', 'Combined 5 Bank - Officer / IT - 2023', 'Combined 5 Bank', 'Officer (IT)', 'BIBM', '03/02/2023', '80 MCQ (IT:75 + Math+GK:25)'),

    (r'Combined 4 Bank.*SO IT \(222 post\) 2023.*Job ID: 10149',
     '02_Bank_IT', '05_Combined_4_Bank_Senior_Officer_IT_2023.md', 'Combined 4 Bank - Senior Officer (IT) - 2023', 'Combined 4 Bank', 'Senior Officer (IT)', 'BIBM', '13/10/2023', '200 Marks (Focus, GK: 40 + IT: 160)'),

    (r'RAKUB.*ANSE \(2 post\) 2023.*Exam date: 03\.11\.2023',
     '02_Bank_IT', '06_RAKUB_Assistant_Network_Security_Engineer_2023.md', 'RAKUB - Assistant Network & Security Engineer - 2023', 'RAKUB', 'Assistant Network & Security Engineer', 'BIBM', '03/11/2023', '200 Marks (Focus, GK: 40 + IT: 160)'),

    (r'RUPALI BANK ANA \(5 Post\) 2023 Job ID: 10166 Exam date: 04\.11\.2023',
     '02_Bank_IT', '07_Rupali_Bank_Assistant_Network_Administrator_2023.md', 'Rupali Bank - Assistant Network Administrator (ANA) - 2023', 'Rupali Bank', 'Assistant Network Administrator (ANA)', 'BIBM', '04/11/2023', '200 Marks (Focus, GK: 40 + IT: 160)'),

    (r'Combined 3 Bank \(10199\).*Assistant Maintenance engineer/Assistant Engineer IT 2024',
     '02_Bank_IT', '08_Combined_3_Bank_10199_AME_AE_IT_2024.md', 'Combined 3 Bank (Job ID 10199) - AME & AE (IT) - 2024', 'Combined 3 Bank', 'AME / AE (IT)', 'BIBM', '2024', '200 Marks'),

    (r'Combined 3 Bank \(10185\).*Senior Officer IT 2024',
     '02_Bank_IT', '09_Combined_3_Bank_10185_Senior_Officer_IT_2024.md', 'Combined 3 Bank (Job ID 10185) - Senior Officer (IT) - 2024', 'Combined 3 Bank', 'Senior Officer (IT)', 'BIBM', '17/05/2024', '200 Marks (80 MCQ + Written)'),

    (r'BSCS \(Sonali & Bank PLC\) Assistant Programmer Officer \(IT\) – 03/01/2026',
     '02_Bank_IT', '10_BSCS_Sonali_Janata_AP_and_Officer_IT_2026.md', 'BSCS (Sonali & Janata Bank) - AP & Officer (IT) - 2026', 'Sonali & Janata Bank', 'Assistant Programmer / Officer (IT)', 'BSCS', '03/01/2026', '200 Marks'),

    (r'Sonali Bank PLC.*Assistant Database Administrator.*Written Exam Question',
     '02_Bank_IT', '11_Sonali_Bank_Assistant_Database_Administrator_2024.md', 'Sonali Bank PLC - Assistant Database Administrator - 2024', 'Sonali Bank PLC', 'Assistant Database Administrator', 'BIBM', '2024', '200 Marks'),

    (r'BSCS – Various Bank Assistant Programmer Date: 17\.01\.2026',
     '02_Bank_IT', '12_BSCS_Various_Bank_Assistant_Programmer_2026.md', 'BSCS Various Banks - Assistant Programmer - 2026', 'Combined Banks', 'Assistant Programmer', 'BIBM/CTI', '17/01/2026', '200 Marks'),

    (r'BSCS-\s*Combined 3 Bank 04 \(Sonali, Janata, Rakub\).*Post: SO\(Written\) Date:16-11-2020',
     '02_Bank_IT', '13_BSCS_Combined_3_Bank_Senior_Officer_2020.md', 'BSCS Combined 3 Bank (Sonali, Janata, RAKUB) - Senior Officer - 2020', 'Combined 3 Bank', 'Senior Officer (IT)', 'BSCS', '16/11/2020', '200 Marks'),

    (r'BSCS -Recruitment 2020.*Combine 2 Bank \(SB &JB\).*Officer IT',
     '02_Bank_IT', '14_BSCS_Combine_2_Bank_Officer_IT_2020.md', 'BSCS Combined 2 Bank (Sonali & Janata) - Officer (IT) - 2020', 'Sonali & Janata Bank', 'Officer (IT)', 'BSCS', '2020', '200 Marks'),

    (r'Assistant Network Engineer \(ANE\) [–\-—\s]*JBL 03 Date: 12\.11\.2020',
     '02_Bank_IT', '15_Janata_Bank_Assistant_Network_Engineer_2020.md', 'Janata Bank - Assistant Network Engineer (ANE) - 2020', 'Janata Bank Limited', 'Assistant Network Engineer (ANE)', 'BSCS', '12/11/2020', '200 Marks (IT: 160 + Non: 40)'),

    (r'Sonali Bank Limited Officer IT 08 Exam Type: Written',
     '02_Bank_IT', '16_Sonali_Bank_Officer_IT_Written_2020.md', 'Sonali Bank Limited - Officer (IT) Written - 2020', 'Sonali Bank Limited', 'Officer (IT)', 'BSCS', '2020', '200 Marks [Dept: 150 + Non: 50]'),

    (r'05 Combined 4 Bank SO IT \(222 post\) 2023 Job ID: 10149 Exam date: 13\.10\.2023',
     '02_Bank_IT', '17_Combined_4_Bank_SO_IT_2023_Part2.md', 'Combined 4 Bank - Senior Officer (IT) Comprehensive Solutions - 2023', 'Combined 4 Bank', 'Senior Officer (IT)', 'BIBM', '13/10/2023', '200 Marks'),

    (r'06 RAKUB ANSE \(2 post\) 2023 Exam date: 03\.11\.2023',
     '02_Bank_IT', '18_RAKUB_ANSE_2023_Part2.md', 'RAKUB - Assistant Network & Security Engineer Solutions - 2023', 'RAKUB', 'Assistant Network & Security Engineer', 'BIBM', '03/11/2023', '200 Marks'),

    (r'07 RUPALI BANK ANA \(5 Post\) 2023 Job ID: 10166 Exam date: 04\.11\.2023',
     '02_Bank_IT', '19_Rupali_Bank_ANA_2023_Part2.md', 'Rupali Bank - Assistant Network Administrator Solutions - 2023', 'Rupali Bank', 'Assistant Network Administrator', 'BIBM', '04/11/2023', '200 Marks'),

    (r'09  Combined 5 bank \(10198\).*Assistant programmer 2024',
     '02_Bank_IT', '20_Combined_5_Bank_10198_Assistant_Programmer_2024.md', 'Combined 5 Bank (Job ID 10198) - Assistant Programmer - 2024', 'Combined 5 Bank', 'Assistant Programmer', 'BIBM', '2024', '200 Marks'),

    (r'11  Combined 3 Bank \(10185\)',
     '02_Bank_IT', '21_Combined_3_Bank_10185_SO_IT_2024_Part2.md', 'Combined 3 Bank (10185) - Senior Officer (IT) Detailed Solutions - 2024', 'Combined 3 Bank', 'Senior Officer (IT)', 'BIBM', '17/05/2024', '200 Marks'),

    (r'12 Combined 2 Bank \(10184\) Officer IT 2024',
     '02_Bank_IT', '22_Combined_2_Bank_10184_Officer_IT_2024.md', 'Combined 2 Bank (10184) - Officer (IT) - 2024', 'Combined 2 Bank', 'Officer (IT)', 'BIBM', '2024', '200 Marks'),

    (r'14 BSCS \(Sonali & Janata Bank PLC\) Assistant Programmer Officer \(IT\) [–\-—\s]*03/01/2026',
     '02_Bank_IT', '23_BSCS_Sonali_Janata_AP_2026_Part2.md', 'BSCS (Sonali & Janata) - AP & Officer (IT) Solutions - 2026', 'Sonali & Janata Bank', 'AP & Officer (IT)', 'BSCS', '03/01/2026', '200 Marks'),

    (r'15 Sonali Bank PLC Assistant Database Administrator Written Exam Question',
     '02_Bank_IT', '24_Sonali_Bank_Assistant_DBA_2024_Part2.md', 'Sonali Bank PLC - Assistant Database Administrator Solutions - 2024', 'Sonali Bank PLC', 'Assistant Database Administrator', 'BIBM', '2024', '200 Marks'),

    (r'Bangladesh Bank Banker\'s Selection Committee Secretariat \(BSCS\) Assistant Maintenance Engineer',
     '02_Bank_IT', '25_Bangladesh_Bank_BSCS_AME_2024.md', 'Bangladesh Bank BSCS - Assistant Maintenance Engineer (200 Marks) - 2024/2026', 'Bangladesh Bank BSCS', 'Assistant Maintenance Engineer / AE (IT)', 'BSCS', '2024/2026', '200 Marks (15 Questions)'),

    (r'Bangladesh Bank Banker\'s Selection Committee Secretariat \(BSCS\) Senior Officer \(IT\), Grade-9.*Job ID-25104',
     '02_Bank_IT', '26_Bangladesh_Bank_BSCS_Senior_Officer_IT_Grade9_2026.md', 'Bangladesh Bank BSCS - Senior Officer (IT) Grade-9 (Job ID 25104) - 2026', 'Bangladesh Bank BSCS', 'Senior Officer (IT) Grade-9', 'BSCS', '2026', '200 Marks'),

    (r'Bangladesh Bank Banker\'s Selection Committee Secretariat \(BSCS\) Officer \(IT\), Grade-10.*Job ID-25105',
     '02_Bank_IT', '27_Bangladesh_Bank_BSCS_Officer_IT_Grade10_2026.md', 'Bangladesh Bank BSCS - Officer (IT) Grade-10 (Job ID 25105) - 2026', 'Bangladesh Bank BSCS', 'Officer (IT) Grade-10', 'BSCS', '31/07/2026', '200 Marks'),

    # 03 BCS and BPSC
    (r'Bangladesh Civil Service\s*[–\-—]?\s*36\*\*.*\(ICT\)\s*Date:\s*2016',
     '03_BCS_and_BPSC', '01_BCS_36th_ICT_Written_2016.md', '36th BCS (ICT) Written Exam - 2016', 'BPSC', 'BCS (ICT Cadre)', 'BPSC', '2016', '200 Marks (3 Hours)'),

    (r'Bangladesh Civil Service\s*[–\-—]?\s*37\*\*.*\(ICT\)\s*Date\s*:\s*2017',
     '03_BCS_and_BPSC', '02_BCS_37th_ICT_Written_2017.md', '37th BCS (ICT) Written Exam - 2017', 'BPSC', 'BCS (ICT Cadre)', 'BPSC', '2017', '200 Marks (3 Hours)'),

    (r'Bangladesh Civil Service\s*[–\-—]?\s*38\*\*.*\(ICT\)\s*Date\s*:\s*2018',
     '03_BCS_and_BPSC', '03_BCS_38th_ICT_Written_2018.md', '38th BCS (ICT) Written Exam - 2018', 'BPSC', 'BCS (ICT Cadre / Lecturer)', 'BPSC', '2018', '200 Marks (3 Hours)'),

    (r'47th BCS Computer Science 8 Subject Code: 971',
     '03_BCS_and_BPSC', '04_BCS_47th_Computer_Science_Subject_971.md', '47th BCS - Computer Science (Subject Code 971) - 200 Marks', 'BPSC', 'Computer Science (Code 971)', 'BPSC', '2024/2025', '200 Marks (4 Hours)'),

    # 04 Telecom and Regulatory
    (r'Bangladesh Telecommunications Company Limited \(BTCL\)\s*Exam Date: 05\.04\.2024',
     '04_Telecom_and_Regulatory', '01_BTCL_JAM_Technical_IT_2024.md', 'BTCL - Junior Assistant Manager (Technical/IT) - 2024', 'BTCL', 'Junior Assistant Manager (Technical)', 'IBA/BTCL', '05/04/2024', '80 Marks (Dept: 65 + Non: 15)'),

    (r'Venue: EUSC Time: 1-hour Total Marks: 80 \(30\+50\) Post: Assistant Director, BTRC Date: 19/02/2021',
     '04_Telecom_and_Regulatory', '02_BTRC_Assistant_Director_Technical_2021.md', 'BTRC - Assistant Director (Technical) - 2021', 'BTRC', 'Assistant Director (Technical)', 'EUSC', '19/02/2021', '80 Marks (30 Non + 50 Dept)'),

    (r'Venue: EUSC Time: 1-hour Total Marks: 80 \(30 MCQ\+50 Written\) Post: Deputy Assistant Director, BTRC Date: 19/02/2021',
     '04_Telecom_and_Regulatory', '03_BTRC_Deputy_Assistant_Director_Technical_2021.md', 'BTRC - Deputy Assistant Director (Technical) - 2021', 'BTRC', 'Deputy Assistant Director (Technical)', 'EUSC', '19/02/2021', '80 Marks (30 MCQ + 50 Written)'),

    (r'BTRC Written Question Post Name: Assistant Director \(Technical\) Exam Date: April 05, 2019',
     '04_Telecom_and_Regulatory', '04_BTRC_Assistant_Director_Technical_2019.md', 'BTRC - Assistant Director (Technical) - 2019', 'BTRC', 'Assistant Director (Technical)', 'BUET', '05/04/2019', '100 Marks'),

    (r'BTRC Written Question Post Name: Deputy Assistant Director \(Technical\) Exam Date: April 05, 2019',
     '04_Telecom_and_Regulatory', '05_BTRC_Deputy_Assistant_Director_Technical_2019.md', 'BTRC - Deputy Assistant Director (Technical) - 2019', 'BTRC', 'Deputy Assistant Director (Technical)', 'BUET', '05/04/2019', '100 Marks'),

    (r'Bangladesh Telecommunication Regulatory Comm.*\(BTRC\).*Post: Assistant Director',
     '04_Telecom_and_Regulatory', '06_BTRC_Assistant_Director_Short_QnA.md', 'BTRC - Assistant Director Question Bank', 'BTRC', 'Assistant Director', 'BTRC', '2019-2021', 'Core Technical Bank'),

    (r'Bangladesh Atomic Energy Regulatory Authority Recruitment Exam – 2021.*Exam Venue : BUET',
     '04_Telecom_and_Regulatory', '07_BAERA_Recruitment_Exam_BUET_2021.md', 'BAERA (Atomic Energy Regulatory Authority) - Recruitment Exam - 2021', 'BAERA', 'Engineer (CSE)', 'BUET', '2021', '100 Marks'),

    (r'Bangladesh Energy Regulatory Authority Exam Taker: BUET Exam date:28/07/2023',
     '04_Telecom_and_Regulatory', '08_BERC_Recruitment_Exam_BUET_2023.md', 'BERC (Energy Regulatory Authority) - Recruitment Exam - 2023', 'BERC', 'Assistant Director / Engineer', 'BUET', '28/07/2023', '100 Marks'),

    # 05 Govt Ministries and Autonomous
    (r'Written Question BRICM AME Exam 24 Feb 2024',
     '05_Govt_Ministries_and_Autonomous', '01_BRICM_Assistant_Maintenance_Engineer_2024.md', 'BRiCM - Assistant Maintenance Engineer (AME) - 2024', 'BRiCM', 'Assistant Maintenance Engineer (AME)', 'BRiCM', '24/02/2024', 'Written Exam'),

    (r'SPARRS',
     '05_Govt_Ministries_and_Autonomous', '02_SPARRSO_Assistant_Engineer_CSE.md', 'SPARRSO - Assistant Engineer (CSE)', 'SPARRSO', 'Assistant Engineer (CSE)', 'SPARRSO', '2021', '100 Marks'),

    (r'বাাংলাদেশ সমরাস্ত্র কারখানা: \(BOF\)-2021.*Post: Assistant Engineer',
     '05_Govt_Ministries_and_Autonomous', '03_BOF_Bangladesh_Ordnance_Factory_AE_2021.md', 'BOF (Bangladesh Ordnance Factory) - Assistant Engineer - 2021', 'BOF', 'Assistant Engineer (CSE)', 'BOF', '2021', '100 Marks'),

    (r'Bangladesh Krira Shikkha Protishtan \(BKSP\).*Post: Assistant Programmer',
     '05_Govt_Ministries_and_Autonomous', '04_BKSP_Assistant_Programmer_2023.md', 'BKSP - Assistant Programmer - 2023', 'BKSP', 'Assistant Programmer', 'BKSP', '2023', 'Written Exam'),

    (r'Dhaka University of Engineering and Technology.*Exam Date: 2020.*Post: Assistant Programmer',
     '05_Govt_Ministries_and_Autonomous', '05_DUET_Assistant_Programmer_2020.md', 'DUET - Assistant Programmer - 2020', 'DUET', 'Assistant Programmer', 'DUET', '2020', 'Dept: 70 Marks'),

    (r'Dhaka University of Engineering and Technology.*Exam Date: 01/02/2025.*Post: Assistant Programmer',
     '05_Govt_Ministries_and_Autonomous', '06_DUET_Assistant_Programmer_2025.md', 'DUET - Assistant Programmer - 2025', 'DUET', 'Assistant Programmer', 'DUET', '01/02/2025', 'Dept: 70 Marks'),

    # 06 Subject-Wise and Special Preparation Banks
    (r'Assistant Engineer \(CSE\) Exam Taker: BUET Time: 10-11 AM Marks: 60 \(Non\)\+Dept \(40\)',
     '06_Subject_Wise_and_Special_Guides', '01_BUET_Assistant_Engineer_CSE_Model_2024.md', 'BUET Pattern - Assistant Engineer (CSE) Model Exam', 'BUET', 'Assistant Engineer (CSE)', 'BUET', 'Model Pattern', '100 Marks (60 Non + 40 Dept)'),

    (r'Software maintenance life cycle\.\s*\[BUET MSC 19\]',
     '06_Subject_Wise_and_Special_Guides', '02_Software_Engineering_and_Networking_Core_Bank.md', 'BUET MSC & Job Preparation - Software Engineering & Networking Bank', 'BUET MSC / Bank / PSU', 'Core CSE Topics', 'Various', 'Comprehensive', 'Multiple Exam Topics'),

    (r'Sample question pattern Previously BUET taken ANE/AHE Questions',
     '06_Subject_Wise_and_Special_Guides', '03_BUET_Pattern_ANE_AHE_Question_Bank.md', 'BUET Pattern - Assistant Network / Hardware Engineer Question Bank', 'BUET Pattern', 'ANE / AHE', 'BUET', 'Comprehensive', 'Full Architecture & Questions'),

    (r'Engineer \(Cyber Security\), NPCBL Cyber Security Job Exam Suggestions',
     '06_Subject_Wise_and_Special_Guides', '04_NPCBL_Cyber_Security_Job_Exam_Guide.md', 'NPCBL & Govt IT - Cyber Security Special Exam Guide', 'NPCBL / Govt IT', 'Cyber Security Engineer', 'NPCBL', 'Special Guide', 'Comprehensive Syllabus & Q&A'),

    (r'Server/Data Center related Job Exam Suggestions',
     '06_Subject_Wise_and_Special_Guides', '05_Server_and_Data_Center_Job_Exam_Guide.md', 'Server & Data Center Architecture Special Exam Guide', 'Data Center / Cloud', 'System / Data Center Admin', 'Bank & Govt IT', 'Special Guide', 'Comprehensive Syllabus & Q&A'),

    (r'Engineer \(Quality\), NPCBL SQA  related Job Exam Suggestions',
     '06_Subject_Wise_and_Special_Guides', '06_SQA_Software_Quality_Assurance_Exam_Guide.md', 'Software Quality Assurance (SQA) Special Exam Guide', 'NPCBL / IT Jobs', 'SQA Engineer', 'Various', 'Special Guide', 'Comprehensive Syllabus & Q&A'),
]

# Match sequentially
matched_sections = []
for pat, cat, fname, title, org, post, taker, date, marks in exam_rules:
    found_idx = None
    for idx, line in enumerate(raw_lines):
        if re.search(pat, line.strip(), re.I):
            found_idx = idx
            break
    if found_idx is not None:
        matched_sections.append({
            'start_line': found_idx,
            'category': cat,
            'filename': fname,
            'title': title,
            'org': org,
            'post': post,
            'taker': taker,
            'date': date,
            'marks': marks
        })

matched_sections.sort(key=lambda x: x['start_line'])

# Base output directory
base_output = os.path.join(os.getcwd(), 'duronto_it_organized')
os.makedirs(base_output, exist_ok=True)

# Process and save each file
all_cleaned_sections = []

for i in range(len(matched_sections)):
    sec = matched_sections[i]
    start = sec['start_line']
    end = matched_sections[i+1]['start_line'] if i+1 < len(matched_sections) else len(raw_lines)
    
    sec['end_line'] = end
    raw_slice = raw_lines[start:end]
    cleaned_content = clean_duronto_lines(raw_slice)
    
    # Target folder
    cat_dir = os.path.join(base_output, sec['category'])
    os.makedirs(cat_dir, exist_ok=True)
    
    file_path = os.path.join(cat_dir, sec['filename'])
    
    # Construct structured header
    file_header = f"# {sec['title']}\n\n"
    file_header += "| Field | Details |\n"
    file_header += "| :--- | :--- |\n"
    file_header += f"| **Organization** | {sec['org']} |\n"
    file_header += f"| **Post Name** | {sec['post']} |\n"
    file_header += f"| **Exam Date** | {sec['date']} |\n"
    file_header += f"| **Exam Taker** | {sec['taker']} |\n"
    file_header += f"| **Marks / Format** | {sec['marks']} |\n"
    file_header += f"| **Source** | Duronto IT Academy / Smart IT Job Solution |\n\n"
    file_header += "---\n\n"
    
    full_file_text = file_header + cleaned_content + "\n"
    
    with open(file_path, 'w', encoding='utf-8') as f_out:
        f_out.write(full_file_text)
        
    sec['file_path'] = file_path
    sec['rel_path'] = os.path.relpath(file_path, os.getcwd()).replace('\\', '/')
    sec['cleaned_text'] = cleaned_content
    sec['word_count'] = len(cleaned_content.split())
    sec['line_count'] = len(cleaned_content.splitlines())
    
    all_cleaned_sections.append(sec)

print(f"Successfully processed and written {len(all_cleaned_sections)} individual markdown files.")

# 4. Generate Master Index Document
index_path = os.path.join(os.getcwd(), 'DURONTO_EXAMS_MASTER_INDEX.md')
with open(index_path, 'w', encoding='utf-8') as f_idx:
    f_idx.write("# Duronto IT Academy - Organized Exam Questions & Solutions\n\n")
    f_idx.write("> **Source Archive:** `Durontoitexq.md` (Cleaned, Organized, and Categorized)\n")
    f_idx.write(f"> **Total Exam Papers & Subject Guides:** {len(all_cleaned_sections)}\n")
    f_idx.write("> **Status:** All watermarks, group promotional spam, repeated headers, and OCR noise removed.\n\n")
    f_idx.write("---\n\n")
    f_idx.write("## Table of Contents\n\n")
    
    # Group by category
    categories_order = [
        ('01_Power_Sector', '⚡ Power Sector IT Job Solutions'),
        ('02_Bank_IT', '🏦 Bank IT Job Solutions (Bangladesh Bank & Commercial Banks)'),
        ('03_BCS_and_BPSC', '🏛️ BCS & BPSC IT Cadre Written Solutions'),
        ('04_Telecom_and_Regulatory', '📡 Telecom & Regulatory Authority Solutions (BTCL, BTRC, BERC, BAERA)'),
        ('05_Govt_Ministries_and_Autonomous', '🏢 Govt Ministries & Autonomous Bodies IT Solutions'),
        ('06_Subject_Wise_and_Special_Guides', '📚 Subject-Wise Question Banks & Special Job Guides')
    ]
    
    for cat_id, cat_title in categories_order:
        cat_exams = [e for e in all_cleaned_sections if e['category'] == cat_id]
        f_idx.write(f"### {cat_title} ({len(cat_exams)} Papers)\n\n")
        f_idx.write("| # | Exam Title | Post | Taker | Date | Marks | File Link |\n")
        f_idx.write("| :-: | :--- | :--- | :--- | :--- | :--- | :--- |\n")
        for idx, e in enumerate(cat_exams, 1):
            f_idx.write(f"| {idx} | **{e['title']}** | {e['post']} | `{e['taker']}` | {e['date']} | {e['marks']} | [View Exam]({e['rel_path']}) |\n")
        f_idx.write("\n")

print(f"Saved master index: {index_path}")

# 5. Generate Durontoitexq_CLEANED.md (Consolidated Master File)
cleaned_master_path = os.path.join(os.getcwd(), 'Durontoitexq_CLEANED.md')
with open(cleaned_master_path, 'w', encoding='utf-8') as f_clean:
    f_clean.write("# Duronto IT Academy - Complete Cleaned Written Exam Questions & Solutions\n\n")
    f_clean.write(f"> **Master Archive containing {len(all_cleaned_sections)} Exam Papers & Modules**\n")
    f_clean.write("> **Completely Cleaned:** No watermarks, no spam links, formatted markdown with syntax-highlighted code.\n\n")
    f_clean.write("## Quick Navigation\n\n")
    for idx, e in enumerate(all_cleaned_sections, 1):
        f_clean.write(f"{idx}. [{e['title']}](#paper-{idx}) — *({e['taker']}, {e['date']})*\n")
    f_clean.write("\n---\n\n")
    
    for idx, e in enumerate(all_cleaned_sections, 1):
        f_clean.write(f"<a name=\"paper-{idx}\"></a>\n\n")
        f_clean.write(f"# {e['title']}\n\n")
        f_clean.write(f"- **Organization:** {e['org']}\n")
        f_clean.write(f"- **Post:** {e['post']}\n")
        f_clean.write(f"- **Exam Taker:** {e['taker']} | **Date:** {e['date']} | **Marks:** {e['marks']}\n\n")
        f_clean.write("---\n\n")
        f_clean.write(e['cleaned_text'])
        f_clean.write("\n\n---\n\n")

print(f"Saved consolidated master file: {cleaned_master_path}")
