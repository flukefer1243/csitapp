from bs4 import BeautifulSoup
import requests
import lxml
import os
import json
from unittest import result
import pyrebase
# from firebase import firebase

headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

proxies = {
    'http': os.getenv('HTTP_PROXY')
}

# params = {
#    "hl": "th",
#     "user": "CcfsliIAAAAJ"
# }


def get_articles(params):
    html = requests.get('https://scholar.google.com/citations',
                        headers=headers, params=params, proxies=proxies).text
    soup = BeautifulSoup(html, 'lxml')
    data = []
    print('Article info:')
    for article_info in soup.select('#gsc_a_b .gsc_a_t'):
        title = article_info.select_one('.gsc_a_at').text
        title_link = f"https://scholar.google.com{article_info.select_one('.gsc_a_at')['href']}"
        authors = article_info.select_one('.gsc_a_at+ .gs_gray').text
        publications = article_info.select_one('.gs_gray+ .gs_gray').text

        data.append({
            'title': title,
            'title_link': title_link,
            'authors': authors,
            'publications': publications,
        })
    # print(f'Title: {title}\nTitle link: {title_link}\nArticle Author(s): {authors}\nArticle Publication(s): {publications}\n')
    return data


def get_timetable1(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'html.parser', from_encoding="windows-874")
    # soup.encode("windows-874")
    tb = soup.find_all(
        "table", {"border": "1", "cellspacing": "0", "cellpadding": "0"})
    return str(tb[0]).replace("¨Ñ¹·Ãì", "จันทร์").replace("ÍÑ§¤ÒÃ", "อังคาร").replace("¾Ø¸", "พุธ").replace("¾ÄËÑÊº´Õ","พฤหัสบดี").replace("ÈØ¡Ãì","ศุกร์").replace("ÍÒ·ÔµÂì","อาทิตย์").replace("àÊÒÃì","เสาร์")

def getData():
    config = {
        "apiKey": "AIzaSyA952ethtCSD2FZsX2rABd6FzsPttYX0ws",
        "authDomain": "csitproject-a3814.firebaseapp.com",
        "databaseURL": "https://csitproject-a3814-default-rtdb.asia-southeast1.firebasedatabase.app",
        "projectId": "csitproject-a3814",
        "storageBucket": "csitproject-a3814.appspot.com",
        "messagingSenderId": "26361500700",
        "appId": "1:26361500700:web:0420b0ff86d117748d3bd9",
        "measurementId": "G-VZQ1RJDWVC"
    }
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    result = db.child("Wansuree_Massagram").child("status").get().val()
    return result
# article = get_articles()
# print(len(data))
# print(data)
# print(json.dumps(article, indent = 2, ensure_ascii = False))
prasart = [
        {
        'namethai' : 'รองศาสตราจารย์ ประศาสตร์ บุญสนอง',
        'nameeng' : 'Associate professor Prasart Boonsanong',
        'position' : 'อาจารย์ (ข้าราชการ)',
        'academicposition' : 'รองศาสตราจารย์',
        'managementposition' : 'ประธานหลักสูตรวิทยาการคอมพิวเตอร์',
        'email' : 'prasartb@nu.ac.th',
        'workroom' : 'SC2-417',
        'scholarid' : 'jjX9xgkAAAAJ',
        'img' : 'fontend/prasart.jpg',
        'timetable' : 'https://reg3.nu.ac.th/registrar/teach_time.asp?officerid=20302&f_cmd=2&officercode=F05002&officername=Assoc%2EProf%2E+Prasart+Boonsnong&remark=&officeremail=prasartb%40nu%2Eac%2Eth'
    },
    [
        'วิทยาศาสตรบัณฑิต(วท.บ.)  คณิตศาสตร์   มหาวิทยาลัยเชียงใหม่  ไทย  1984',
        'พัฒนบริหารศาสตรมหาบัณฑิต(พบ.ม.)   สถิติประยุกต์  สถาบันบัณฑิตพัฒนบริหารศาสตร์  ไทย  1991',
    ],

]
chakkrit = [
    {
        'namethai' : 'รองศาสตราจารย์ ดร.จักรกฤษณ์ เสน่ห์ นมะหุต',
        'nameeng' : 'Associate professor Chakkrit Snae Namahoot, Ph.D.',
        'position' : 'อาจารย์ (ข้าราชการ)',
        'academicposition' : 'รองศาสตราจารย์',
        'managementposition' : 'ผู้รับผิดชอบหลักสูตร วท.ม.วิทยาการคอมพิวเตอร์',
        'email' : 'chakkrits@nu.ac.th',
        'workroom' : 'SC2-301',
        'scholarid' : 'M9YAt9QAAAAJ',
        'img' : 'fontend/chakkrit.jpg',
        'timetable' : 'https://reg3.nu.ac.th/registrar/teach_time.asp?officerid=20314&f_cmd=2&officercode=F05003&officername=Assoc%2EProf%2EDr%2E+Chakkrit+Snae&remark=&officeremail=chakkrits%40nu%2Eac%2Eth'
    },
    [
        'วิทยาศาสตรบัณฑิต(วท.บ.)  คณิตศาสตร์  มหาวิทยาลัยนเรศวร  ไทย  1995',
        'Master of Science(M.S.)  Computing Science  University of Newcastle upon tyne  อังกฤษ  1999',
        'Doctor of Philosophy(Ph.D.)  Computer Science  The University of Liverpool  อังกฤษ  2006',
    ],


]
ekkasit = [
        {
        'namethai' : 'ดร.เอกสิทธิ์ เทียมแก้ว',
        'nameeng' : 'Ekkasit Ttiamkaew, Ph.D.',
        'position' : 'อาจารย์ (ข้าราชการ)',
        'academicposition' : 'อาจารย์',
        'managementposition' : 'ผู้รับผิดชอบหลักสูตร วท.บ.วิทยาการคอมพิวเตอร์',
        'email' : 'ekkasitt@nu.ac.th',
        'workroom' : 'SC2-301',
        'scholarid' : 'k3lg7OAAAAAJ',
        'img' : 'fontend/ekkasit.jpg',
        'timetable' : 'https://reg3.nu.ac.th/registrar/teach_time.asp?officerid=20321&f_cmd=2&officercode=F05007&officername=Dr%2E+Ekkasit+Tiamkaew&remark=&officeremail=ekkasit%2Etiamkaew%40gmail%2Ecom'
    },
    [
        '2537 : ปริญญาตรี :  วิศวกรรมศาสตร์คอมพิวเตอร์ [ มหาวิทยาลัยพระจอมเกล้าธนบุรี ]',
        '2540 : ปริญญาโท :  วิศวกรรมศาสตร์คอมพิวเตอร์ [ University of Massachusetts, Lowell, USA ]',
        '2548 : ปริญญาเอก :  วิศวกรรมศาสตร์คอมพิวเตอร์ [ University of Nevada, Reno, USA ]',
    ],

]
nattavadee = [
     {
        'namethai' : 'อาจารย์ณัฐวดี หงษ์บุญมี',
        'nameeng' : 'Miss Nattavadee Hongboonmee',
        'position' : 'อาจารย์ (ข้าราชการ)',
        'academicposition' : 'อาจารย์',
        'managementposition' : 'ผู้ช่วยหัวหน้าภาควิชาวิทยาการคอมพิวเตอร์และเทคโนโลยีสารสนเทศ',
        'email' : 'nattavadeeho@nu.ac.th',
        'workroom' : 'Sc2-317',
        'scholarid' : 'fy4oSlcAAAAJ',
        'img' : 'fontend/nattavadee.jpg',
        'timetable' : 'https://reg3.nu.ac.th/registrar/teach_time.asp?officerid=20329&f_cmd=2&officercode=F05008&officername=Miss+Nattavadee+Hongbonmee&remark=&officeremail=nattavadeeho%40nu%2Eac%2Eth'
    },
    [
        'เทคโนโลยีสารสนเทศ(วท.ม.) สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง ไทย 2546',
        'วิทยาการคอมพิวเตอร์(วท.บ.) มหาวิทยาลัยนเรศวร ไทย 2541',        
    ],

]
wuttipong = [
     {
        'namethai' : 'อาจารย์วุฒิพงษ์ เรือนทอง',
        'nameeng' : 'Mr.Wuttipong Ruanthong',
        'position' : 'อาจารย์ (ข้าราชการ)',
        'academicposition' : 'อาจารย์',
        'managementposition' : 'รองหัวหน้าภาควิชาวิทยาการคอมพิวเตอร์และเทคโนโลยีสารสนเทศ',
        'email' : 'wuttipongr@nu.ac.th',
        'workroom' : 'SC2-401',
        'scholarid' : 'PgZZHKgAAAAJ',
        'img' : 'fontend/wuttipong.jpg',
        'timetable' : 'https://reg3.nu.ac.th/registrar/teach_time.asp?officerid=20330&f_cmd=2&officercode=F05009&officername=Mr%2E+Wuttipong+Ruanthong&remark=&officeremail=wuttipongr%40nu%2Eac%2Eth'
    },
    [
        'วิทยาศาสตรบัณฑิต(วท.บ.) วิทยาการคอมพิวเตอร์  มหาวิทยาลัยนเรศวร  ไทย  1998',
        'วิทยาศาสตรมหาบัณฑิต(วท.ม.) วิทยาศาสตร์คอมพิวเตอร์  จุฬาลงกรณ์มหาวิทยาลัย  ไทย  2001',        
    ],

]
janjira = [
       {
        'namethai' : 'ผู้ช่วยศาสตราจารย์ ดร.จันทร์จิรา พยัคฆ์เพศ',
        'nameeng' : 'Assistant professor Janjira Payakpate, Ph.D.',
        'position' : 'อาจารย์ (ข้าราชการ)',
        'academicposition' : 'ผู้ช่วยศาสตราจารย์  ',
        'managementposition' : 'ผู้ช่วยหัวหน้าภาควิชาวิทยาการคอมพิวเตอร์และเทคโนโลยีสารสนเทศ',
        'email' : 'janjirap@nu.ac.th',
        'workroom' : 'SC2-317',
        'scholarid' : 'MJgQbgIAAAAJ',
        'img' : 'fontend/janjira.jpg',
        'timetable' : 'https://reg3.nu.ac.th/registrar/teach_time.asp?officerid=20331&f_cmd=2&officercode=F05010&officername=Asst%2EProf%2EDr%2E+Janjira+Payakpate&remark=&officeremail=janjirap'
    },
    [
        'วิทยาศาสตรบัณฑิต(วท.บ.)  วิทยาการคอมพิวเตอร์  มหาวิทยาลัยนเรศวร  ไทย  1998',
        'Master of Science(M.S.)  Computer Science  University of Wollongong  ออสเตรเลีย  2001',  
        'Doctor of Philosophy(Ph.D.)  Information Technology  Murdoch University  ออสเตรเลีย  2009',      
    ],

]
adirek = [
          {
        'namethai' : 'อาจารย์อดิเรก รุ่งรังษี',
        'nameeng' : ' Mr.Adirek Roongrungsi',
        'position' : 'อาจารย์ (ข้าราชการ)',
        'academicposition' : 'อาจารย์',
        'managementposition' : 'ผู้รับผิดชอบหลักสูตร วท.บ.เทคโนโลยีสารสนเทศ',
        'email' : 'adirekr@nu.ac.th',
        'workroom' : 'SC2-401',
        'scholarid' : 'aipQHNoAAAAJ',
        'img' : 'fontend/adirek.jpg',
        'timetable' : 'https://reg3.nu.ac.th/registrar/teach_time.asp?officerid=20335&f_cmd=2&officercode=F05011&officername=Mr%2E+Adirek+Roongrungsi&remark=%B5%D4%B4%B5%E8%CD%CD%D2%A8%D2%C3%C2%EC%B4%E8%C7%B9+%E3%CB%E9%B5%D4%B4%B5%E8%CD%BC%E8%D2%B9%E2%B7%C3%C8%D1%BE%B7%EC%C1%D7%CD%B6%D7%CD%B9%D0%A4%C3%D1%BA&officeremail=adirekr%40nu%2Eac%2Eth'
    },
    [
        'วิทยาศาสตรบัณฑิต(วท.บ.) สัตวศาสตร์  สถาบันเทคโนโลยีราชมงคล วิทยาเขตบางพระ  ไทย  1994',
        'Master of Computing(M.C.) Griffith University  ออสเตรเลีย  1997',       
    ],

]
anongporn = [
      {
        'namethai' : 'ผู้ช่วยศาสตราจารย์ ดร.อนงค์พร ไศลวรากุล',
        'nameeng' : 'Assistant professor Anongporn Salaiwarakul, Ph.D.',
        'position' : 'อาจารย์ (ข้าราชการ)',
        'academicposition' : 'ผู้ช่วยศาสตราจารย์',
        'managementposition' : 'ผู้รับผิดชอบหลักสูตร วท.ม.วิทยาการคอมพิวเตอร์',
        'email' : 'anongporns@nu.ac.th',
        'workroom' : 'SC2-406',
        'scholarid' : 'null',
        'img' : 'fontend/anongporn.jpg',
        'timetable' : 'https://reg3.nu.ac.th/registrar/teach_time.asp?officerid=20336&f_cmd=2&officercode=F05012&officername=Asst%2EProf%2EDr%2E+Anongporn+Salaiwarakul&remark=&officeremail=anongporns%40nu%2Eac%2Eth'
    },
    [
        'วิทยาศาสตรบัณฑิต(วท.บ.)  วิทยาศาสตร์คอมพิวเตอร์  มหาวิทยาลัยอัสสัมชัญ  ไทย  1997',
        'วิทยาศาสตรมหาบัณฑิต(วท.ม.)  วิทยาศาสตร์คอมพิวเตอร์  จุฬาลงกรณ์มหาวิทยาลัย  ไทย  2002', 
        'Doctor of Philosophy(Ph.D.)  Computer Science  University of Birmingham  อังกฤษ  2010',      
    ],

]
tawin = [
      {
        'namethai' : 'ผู้ช่วยศาสตราจารย์เทวิน ธนะวงษ์',
        'nameeng' : 'Assistant professor Tawin Tanawong',
        'position' : 'พนักงานมหาวิทยาลัย (สายวิชาการ)',
        'academicposition' : 'ผู้ช่วยศาสตราจารย์',
        'managementposition' : 'ประธานหลักสูตรสาขาเทคโนโลยีสารสนเทศ',
        'email' : 'tawint@nu.ac.th',
        'workroom' : 'SC2-417',
        'scholarid' : 'Ar1Nj3wAAAAJ',
        'img' : 'fontend/tawin.jpg',
        'timetable' : 'https://reg3.nu.ac.th/registrar/teach_time.asp?officerid=20342&f_cmd=2&officercode=F05013&officername=Asst%2EProf%2E+TAWIN+TANAWONG&remark=&officeremail=tawint'
    },
    [
        'วิทยาศาสตรบัณฑิต(วท.บ.)  สถิติ  มหาวิทยาลัยเชียงใหม่  ไทย  1995',
        'วิศวกรรมศาสตรมหาบัณฑิต(วศ.ม.)  วิศวกรรมไฟฟ้า  สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง  ไทย  2001',       
    ],


]
kreangsak = [
    {
        'namethai' : 'ผู้ช่วยศาสตราจารย์ ดร.เกรียงศักดิ์ เตมีย์',
        'nameeng' : 'Assistant professor Kreangsak Tamee, Ph.D.',
        'position' : 'พนักงานมหาวิทยาลัย (สายวิชาการ)',
        'academicposition' : 'ผู้ช่วยศาสตราจารย์',
        'managementposition' : 'ผู้ช่วยคณบดีด้านเทคโนโลยีสารสนเทศ',
        'email' : 'kreangsakt@nu.ac.th',
        'workroom' : 'Sc2-401',
        'scholarid' : 'dDM6fasAAAAJ',
        'img' : 'fontend/kreangsak.jpg',
        'timetable' : 'https://reg3.nu.ac.th/registrar/teach_time.asp?officerid=20343&f_cmd=2&officercode=F05014&officername=Asst%2EProf%2EDr%2E+KREANGSAK+TAMEE&remark=&officeremail=kreangsakt'
    },
    [
        'วิทยาศาสตรบัณฑิต(วท.บ.)  ฟิสิกส์  มหาวิทยาลัยเชียงใหม่  ไทย  1997',
        'วิศวกรรมศาสตรมหาบัณฑิต(วศ.ม.)  วิศวกรรมไฟฟ้า  สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง  ไทย  2001',
        'วิศวกรรมศาสตรดุษฎีบัณฑิต(วศ.ด.)  วิศวกรรมไฟฟ้า  สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง  ไทย  2011',       
    ],

]
jaratsri = [
      {
        'namethai' : 'ผู้ช่วยศาสตราจารย์ ดร.จรัสศรี รุ่งรัตนาอุบล',
        'nameeng' : 'Assistant professor Jaratsri Rungrattanaubol, Ph.D.',
        'position' : 'พนักงานมหาวิทยาลัย (สายวิชาการ)',
        'academicposition' : 'ผู้ช่วยศาสตราจารย์',
        'managementposition' : 'หัวหน้าภาควิทยาการคอมพิวเตอร์และเทคโนโลยีสารเทศ',
        'email' : 'jaratsrir@nu.ac.th',
        'workroom' : 'Sc2-317',
        'scholarid' : 'FdV0HBkAAAAJ',
        'img' : 'fontend/jaratsri.jpg',
        'timetable' : 'https://reg3.nu.ac.th/registrar/teach_time.asp?officerid=20346&f_cmd=2&officercode=F05015&officername=Asst%2EProf%2EDr%2E+JARATSRI+RUNGRATTANAUBOL&remark=&officeremail=jaratsrir%40nu%2Eac%2Eth'
    },
    [
        'Bachelor of Engineering(B.E.)   Second class honours in computing   University of London  อังกฤษ',
        'Master of Science(M.S.)   Parallel Computers and Computation   University of Warwick  อังกฤษ  1998',
        'Doctor of Philosophy(Ph.D.)   Computer Science   University of Warwick  อังกฤษ',       
    ],

]
winai = [
          {
        'namethai' : 'ผู้ช่วยศาสตราจารย์ ดร.วินัย วงษ์ไทย',
        'nameeng' : 'Assistant professor Winai Wongthai, Ph.D.',
        'position' : 'พนักงานมหาวิทยาลัย (สายวิชาการ)',
        'academicposition' : 'ผู้ช่วยศาสตราจารย์',
        'managementposition' : 'ผู้รับผิดชอบหลักสูตร วท.ม.วิทยาการคอมพิวเตอร์',
        'email' : 'winaiw@nu.ac.th',
        'workroom' : 'Sc2-417',
        'scholarid' : 'zosIMyAAAAAJ',
        'img' : 'fontend/winai.jpg',
        'timetable' : 'https://reg3.nu.ac.th/registrar/teach_time.asp?officerid=20348&f_cmd=2&officercode=F05016&officername=Asst%2EProf%2E+WINAI+WONGTHAI&remark=&officeremail=winaiw%40nu%2Eac%2Eth'
    },
    [
        'ปริญญาตรี วิทยาศาสตร์ วิทยาการคอมพิวเตอร์ มหาวิทยาลัยนเรศวร 2543',
        'ปริญญาโท Science Computer Science สถาบันเทคโนโลยีแห่งเอเชีย 2545',
        'ปริญญาโท System Design of Internet Applications  University of Newcastle upon tyne 2552', 
        'ปริญญาเอก Science  Computer Science  University of Newcastle upon tyne 2557',      
    ],

]
kraisak = [
              {
        'namethai' : 'รองศาสตราจารย์ ดร.ไกรศักดิ์ เกษร',
        'nameeng' : 'Associate professor Kraisak Kesorn, Ph.D.',
        'position' : 'พนักงานมหาวิทยาลัย (สายวิชาการ)',
        'academicposition' : 'รองศาสตราจารย์',
        'managementposition' : 'ผู้ช่วยหัวหน้าภาควิชาวิทยาการคอมพิวเตอร์และเทคโนโลยีสารสนเทศ',
        'email' : 'kraisakk@nu.ac.th',
        'workroom' : 'Sc2-401',
        'scholarid' : 'DZ3WuzUAAAAJ',
        'img' : 'fontend/kraisak.jpg',
        'timetable' : 'https://reg3.nu.ac.th/registrar/teach_time.asp?officerid=20351&f_cmd=2&officercode=F05018&officername=Assoc%2EProf%2EDr%2E+KRAISAK+KESORN&remark=&officeremail=kraisakk%40nu%2Eac%2Eth'
    },
    [
        'วิทยาศาสตรบัณฑิต(วท.บ.) วิทยาการคอมพิวเตอร์ มหาวิทยาลัยเชียงใหม่  ไทย  1998',
        'วิทยาศาสตรมหาบัณฑิต(วท.ม.) เทคโนโลยีสารสนเทศ สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง ไทย 2003',
        'Doctor of Philosophy(Ph.D.) Electronic Engineering Queen Mary, University of London อังกฤษ 2010',     
    ],

]
sanya = [
              {
        'namethai' : 'ผู้ช่วยศาสตราจารย์ ดร.สัญญา เครือหงษ์',
        'nameeng' : 'Assistant professor Sanya Khruahong, Ph.D.',
        'position' : 'พนักงานมหาวิทยาลัย (สายวิชาการ)',
        'academicposition' : 'ผู้ช่วยศาสตราจารย์',
        'managementposition' : 'หัวหน้าภาควิชาวิทยาการคอมพิวเตอร์และเทคโนโลยีสารสนเทศ',
        'email' : 'sanyak@nu.ac.th',
        'workroom' : 'ห้องภาควิชาฯ',
        'scholarid' : 'CcfsliIAAAAJ',
        'img' : 'fontend/sanya.png',
        'timetable' : 'https://reg3.nu.ac.th/registrar/teach_time.asp?officerid=20352&f_cmd=2&officercode=F05019&officername=Asst%2EProf%2EDr%2E+Sanya+Khruahong&remark=http%3A%2F%2Fwww%2E9sanya%2Ecom&officeremail=sanyak%40nu%2Eac%2Eth'
    },
    [
        'วิทยาศาสตรบัณฑิต (วท.บ.)  วิทยาการคอมพิวเตอร์  สถาบันราชภัฏพิบูลสงคราม, ไทย,  1998',
        'วิทยาศาสตรมหาบัณฑิต (วท.ม.)  เทคโนโลยีสารสนเทศ  สถาบันเทคโนโลยีพระจอมเกล้าพระนครเหนือ,  ไทย,  2003',
        'Doctor of Philosophy (Ph.D.)  Computer Systems, University of Technology Sydney, ออสเตรเลีย,  2019',
        'บริหารธุรกิจมหาบัณฑิต (บธ.ม.) การบริหารเทคโนโลยีสารสนเทศเชิงกลยุทธ์ มหาวิทยาลัยนเรศวร, ไทย, 2020',     
    ],

]
sutasinee = [
     {
        'namethai' : 'ผู้ช่วยศาสตราจารย์ ดร.สุธาสินี จิตต์อนันต์',
        'nameeng' : 'Assistant professor Sutasinee Jitanan, Ph.D.',
        'position' : 'พนักงานมหาวิทยาลัย (สายวิชาการ)',
        'academicposition' : 'ผู้ช่วยศาสตราจารย์',
        'managementposition' : 'ผู้รับผิดชอบหลักสูตร วท.บ.เทคโนโลยีสารสนเทศ',
        'email' : 'sutasineec@nu.ac.th',
        'workroom' : ' Sc2-406',
        'scholarid' : '1z0iPloAAAAJ',
        'img' : 'fontend/sutasinee.jpg',
        'timetable' : 'https://reg3.nu.ac.th/registrar/teach_time.asp?officerid=32111&f_cmd=2&officercode=F05020&officername=%BC%C8%2E%B4%C3%2E+%CA%D8%B8%D2%CA%D4%B9%D5+%A8%D4%B5%B5%EC%CD%B9%D1%B9%B5%EC&remark=&officeremail=sutasineec'
    },
    [
        'วิทยาศาสตรบัณฑิต(วท.บ.)  วิทยาการคอมพิวเตอร์  มหาวิทยาลัยเชียงใหม่  ไทย 1996',
        'วิทยาศาสตรมหาบัณฑิต(วท.ม.)  เทคโนโลยีสารสนเทศ  สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง  ไทย  2002',
        'วิศวกรรมศาสตรดุษฎีบัณฑิต(วศ.ด.)  วิศวกรรมคอมพิวเตอร์  มหาวิทยาลัยเกษตรศาสตร์  ไทย  2015',
    ],


]
wansuree = [
    {
        'namethai' : 'ดร.วันสุรีย์ มาศกรัม',
        'nameeng' : 'Wansuree Massagram, Ph.D',
        'position' : 'พนักงานมหาวิทยาลัย (สายวิชาการ)',
        'academicposition' : 'อาจารย์',
        'managementposition' : 'ผู้รับผิดชอบหลักสูตร วท.ม.วิทยาการคอมพิวเตอร์',
        'email' : 'wansureem@nu.ac.th',
        'workroom' : 'SC2-306',
        'scholarid' : '774u2yEAAAAJ',
        'img' : 'fontend/wansuree.jpg',
        'timetable' : 'https://reg9.nu.ac.th/registrar/teach_time.asp?officerid=36051&f_cmd=2&officercode=F05021&officername=%B4%C3%2E+%C7%D1%B9%CA%D8%C3%D5%C2%EC+%C1%D2%C8%A1%C3%D1%C1&remark=&officeremail=wansureem'
    },
    [
        'Bachelor of science(B.Sc.) Electrical and Computer Engineering Carnegie Mellon University สหรัฐอเมริกา 2001',
        'Master of Science(M.Sc.) Electrical and Computer Engineering Carnegie Mellon University สหรัฐอเมริกา 2002',
        'Doctor of Philosophy(Ph.D.) Electrical Engineering University of Hawaii at Manoa 2008'
    ],
    

]
phisetphong = [
    {
        'namethai' : 'อาจารย์พิเศษพงศ์ สุธาพันธ์',
        'nameeng' : 'Mr. Phisetphong Suthaphan',
        'position' : 'พนักงานมหาวิทยาลัย (สายวิชาการ)',
        'academicposition' : 'ไมีมี',
        'managementposition' : 'ไม่มี',
        'email' : 'phisetphongs@nu.ac.th',
        'workroom' : ' Sc2-306',
        'scholarid' : 'Zb5CwNQAAAAJ',
        'img' : 'fontend/phisetphong.jpg',
        'timetable' : 'https://reg3.nu.ac.th/registrar/teach_time.asp?officerid=38404&f_cmd=2&officercode=F05022&officername=%B9%D2%C2+%BE%D4%E0%C8%C9%BE%A7%C8%EC+%CA%D8%B8%D2%BE%D1%B9%B8%EC&remark=&officeremail=phisetphongs'
    },
    [
        'วิทยาศาสตรบัณฑิต(วท.บ.) สถิติ  มหาวิทยาลัยศรีนครินทรวิโรฒ  ไทย  1994',
        'วิทยาศาสตรมหาบัณฑิต(วท.ม.) วิทยาการคอมพิวเตอร์และเทคโนโลยีสารสนเทศ  สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง  ไทย  2001',
    ],

]
duangduen = [
    {
        'namethai' : 'ผู้ช่วยศาสตราจารย์ ดร.ดวงเดือน อัศวสุธีรกุล',
        'nameeng' : 'Assistant professor Duangduen Asavasuthirakul, Ph.D.',
        'position' : 'พนักงานมหาวิทยาลัย (สายวิชาการ)',
        'academicposition' : 'ผู้ช่วยศาสตราจารย์',
        'managementposition' : 'ผู้ช่วยหัวหน้าภาควิชาวิทยาการคอมพิวเตอร์และเทคโนโลยีสารสนเทศ',
        'email' : 'duangduenr@nu.ac.th',
        'workroom' : 'Sc2-406',
        'scholarid' : 'vV-shaYAAAAJ',
        'img' : 'fontend/duangduen.jpg',
        'timetable' : 'https://reg3.nu.ac.th/registrar/teach_time.asp?officerid=44550&f_cmd=2&officercode=F05023&officername=%BC%C8%2E%B4%C3%2E+%B4%C7%A7%E0%B4%D7%CD%B9+%CD%D1%C8%C7%CA%D8%B8%D5%C3%A1%D8%C5&remark=&officeremail=duangduenr%40nu%2Eac%2Eth'
    },
    [
        'วิศวกรรมศาสตรบัณฑิต(วศ.บ.) วิศวกรรมไฟฟ้า มหาวิทยาลัยเชียงใหม่ ไทย 2002',
        'Master of Science(M.Sc.) Information Science University of Pittsburgh สหรัฐอเมริกา 2006',
        'Doctor of Philosophy(Ph.D.) Information Science University of Pittsburgh สหรัฐอเมริกา 2011',
    ],

]
thanathorn = [
    {
        'namethai' : 'ผู้ช่วยศาสตราจารย์ ดร.ธนะธร พ่อค้า',
        'nameeng' : 'Assistant professor Thanathorn Phoka, Ph.D.',
        'position' : 'พนักงานมหาวิทยาลัย (สายวิชาการ)',
        'academicposition' : 'ผู้ช่วยศาสตราจารย์',
        'managementposition' : 'ผู้ช่วยคณบดีด้านนวัตกรรมการเรียนรู้',
        'email' : 'thanathornp@nu.ac.th',
        'workroom' : 'Sc2-306',
        'scholarid' : 'WzhDb0V-gkYC',
        'img' : 'fontend/thanathorn.jpg',
        'timetable' : 'https://reg3.nu.ac.th/registrar/teach_time.asp?officerid=50816&f_cmd=2&officercode=F05024&officername=%BC%C8%2E%B4%C3%2E+%B8%B9%D0%B8%C3+%BE%E8%CD%A4%E9%D2&remark=&officeremail='
    },
    [
        'วิศวกรรมศาสตรบัณฑิต(วศ.บ.) วิศวกรรมคอมพิวเตอร์ จุฬาลงกรณ์มหาวิทยาลัย ไทย 2002',
        'วิศวกรรมศาสตรมหาบัณฑิต(วศ.ม.) วิศวกรรมคอมพิวเตอร์ จุฬาลงกรณ์มหาวิทยาลัย ไทย 2004',
        'วิศวกรรมศาสตรดุษฎีบัณฑิต(วศ.ด.) วิศวกรรมคอมพิวเตอร์ จุฬาลงกรณ์มหาวิทยาลัย ไทย 2011',
    ],


]
nattapon = [
    {
        'namethai' : 'ดร. ณัฐพล คุ้มใหญ่โต',
        'nameeng' : 'Nattapon Kumyaito, Ph.D.',
        'position' : 'พนักงานมหาวิทยาลัย (สายวิชาการ)',
        'academicposition' : 'ไม่มี',
        'managementposition' : 'ไม่มี',
        'email' : 'nattaponk@nu.ac.th',
        'workroom' : 'Sc2-306',
        'scholarid' : 'MI387QEAAAAJ',
        'img' : 'fontend/nattapon.jpg',
        'timetable' : 'https://reg3.nu.ac.th/registrar/teach_time.asp?officerid=55294&f_cmd=2&officercode=F05026&officername=%B4%C3%2E+%B3%D1%B0%BE%C5+%A4%D8%E9%C1%E3%CB%AD%E8%E2%B5&remark=&officeremail=nattaponk'
    },
    [
        'วิศวกรรมศาสตรบัณฑิต(วศ.บ.) วิศวกรรมคอมพิวเตอร์ จุฬาลงกรณ์มหาวิทยาลัย ไทย 2002',
        'วิศวกรรมศาสตรมหาบัณฑิต(วศ.ม.) วิศวกรรมคอมพิวเตอร์ จุฬาลงกรณ์มหาวิทยาลัย ไทย 2004',
        'วิศวกรรมศาสตรดุษฎีบัณฑิต(วศ.ด.) วิศวกรรมคอมพิวเตอร์ จุฬาลงกรณ์มหาวิทยาลัย ไทย 2011',
    ],

]
antony = [
    {
        'namethai' : 'Assistant professor Antony Harfield , Ph.D.',
        'nameeng' : 'Assistant professor Antony Harfield , Ph.D.',
        'position' : 'อาจารย์ (ผู้มีความรู้ความสามารถพิเศษ)',
        'academicposition' : 'Assistant professor',
        'managementposition' : 'ผู้รับผิดชอบหลักสูตร วท.บ.เทคโนโลยีสารสนเทศ',
        'email' : 'antonyh@nu.ac.th',
        'workroom' : 'Sc2-301',
        'scholarid' : 'Ure1mb8AAAAJ',
        'img' : 'fontend/antony.jpg',
        'timetable' : 'https://reg3.nu.ac.th/registrar/teach_time.asp?officerid=41871&f_cmd=2&officercode=F05X07&officername=%BC%C8%2E%28%BE%D4%E0%C8%C9%29+%B4%C3%2E+Antony+Harfield&remark=&officeremail=antonyh'
    },
    [
        'Doctor of Philosophy(Ph.D.) Computer Science University of Warwick อังกฤษ 2008',
        'B.Sc.Computer Science University of Warwick อังกฤษ 2004',
    ],

]