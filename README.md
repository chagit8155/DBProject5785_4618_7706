# DBProject5785_4618_7706

## תוכן עניינים  
- [שלב 1: תכנון ובניית מסד הנתונים](#שלב-1-תכנון-ובניית-מסד-הנתונים)  
  - [מבוא](#מבוא)  
  - [ERD (תרשים ישויות-קשרים)](#erd-תרשים-ישויות-קשרים)  
  - [DSD (תרשים מבנה נתונים)](#dsd-תרשים-מבנה-נתונים)  
  - [סקריפטים ב-SQL](#סקריפטים-ב-sql)  
  - [נתונים](#נתונים)  
  - [גיבוי](#גיבוי)  
- [שלב 2: אינטגרציה ושאילתות](#שלב-2-אינטגרציה)
  - [שאילתות](#שאילתות)
  - [אילוצים](#אילוצים)
  - [rollback  ו commit ](#rollback  ו commit )
  - [גיבוי מעודכן](#גיבוי מעודכן)


## שלב 1: תכנון ובניית מסד הנתונים  

### מבוא

# מערכת ניהול מכון כושר

## תיאור הפרויקט

מערכת ניהול מכון הכושר נועדה לייעל את תהליך הארגון והמעקב אחר מידע חיוני הקשור למנויים, מדריכים, סוגי שיעורים, ציוד וחדרים. מערכת זו מאפשרת למנהלי מכון הכושר, למדריכים ולמנויים גישה נוחה למידע מעודכן, תוך שמירה על מבנה נתונים יעיל ומסודר.

## מטרת המערכת

מסד נתונים זה משמש כפתרון מובנה ואמין למכוני כושר על מנת:

- לנהל רשימת מנויים, כולל תאריכי רישום ותוקף המנוי.
- לקשר מדריכים מוסמכים לסוגי שיעורים שונים בהתאם לרמת הניסיון הנדרשת.
- לארגן שיעורים על פי ימים בשבוע, שעות, סוגים והדרישות המיוחדות לכל שיעור.
- לנהל את החדרים הזמינים במכון ולהבטיח שהקיבולת מתאימה לשיעורים המתוכננים.
- לעקוב אחר ציוד הכושר, כולל מצבו ומיקומו.

## מקרי שימוש פוטנציאליים

- **מנהלי מכון הכושר** יכולים להשתמש במערכת לניהול מנויים, שיעורים, מדריכים וחדרים באופן יעיל ומסודר.
- **מדריכים** יכולים לבדוק אילו שיעורים הם מוסמכים להעביר, אילו חדרים זמינים ולהירשם להעברת שיעורים בהתאם לניסיונם.
- **מנויים** יכולים להירשם לשיעורים השונים בהתאם למגדרם ולהעדפותיהם ולוודא שהשיעורים מותאמים לרמתם ולצרכיהם.
- **צוות המכון** יכול לעקוב אחר מצב הציוד ולוודא תחזוקה שוטפת של חדרי הכושר והאביזרים.

מסד נתונים זה מסייע לייעול הניהול, לשיפור הארגון ולשמירה על חוויית אימון אופטימלית עבור כלל המשתמשים.


###  ERD (תרשים ישויות-קשרים)    
![ERD (תרשים ישויות-קשרים)](Stage1/ERDAndDSD/ERD.png)  

###  DSD  (תרשים מבנה נתונים)
![DSD (תרשים מבנה נתונים)](Stage1/ERDAndDSD/DSD.png)  

### סקריפטים ב-SQL  
ספק את סקריפטי ה-SQL הבאים:  
- **סקריפט יצירת טבלאות** - הסקריפט ליצירת טבלאות מסד הנתונים זמין במאגר:  

📜 **[צפייה ב-create_tables.sql](Stage1/scripts/createTable.sql)**  

- **סקריפט הוספת נתונים** - הסקריפט להזנת נתונים לטבלאות מסד 


הנתונים זמין במאגר:  

📜 **[צפייה ב-insert_tables.sql](Stage1/scripts/insertTables.sql)**  

- **סקריפט מחיקת טבלאות** - הסקריפט למחיקת כל הטבלאות זמין במאגר:  

📜 **[צפייה ב-drop_tables.sql](Stage1/scripts/dropTables.sql)**  

- **סקריפט שליפת כל הנתונים** - הסקריפט לשליפת כל הנתונים מכל הטבלאות זמין במאגר:  

📜 **[צפייה ב-selectAll_tables.sql](Stage1/scripts/selectAll.sql)**

### נתונים  
#### כלי ראשון: שימוש ב-[Mockaroo](https://www.mockaroo.com/) ליצירת קובץ CSV  
##### הזנת נתונים לטבלת person  
- טווח מזהי person: 1-800  
📜 [צפייה ב-`Person.csv`](Stage1/mockData/Person.csv)  

##### הזנת נתונים לטבלת Member  
- טווח מזהי person: 1-400  
📜 [צפייה ב-`Member.csv`](Stage1/mockData/Member.csv)  
 
##### הזנת נתונים לטבלת Trainer
- טווח מזהי person: 401-800  
- נוסחת מזהה איש: `this + 400`  
📜 [צפייה ב-`Trainer.csv`](Stage1/mockData/Trainer.csv)  


### דוגמה להמחשת העבודה באתר עבור הטבלה Person: 
- הגדרת סוגי תכונות הישות ושמותיהם באתר
![image](Stage1/mockData/1.jpeg)
- העלאת הקובץ שנוצר למאגר ע"י עמידה על הטבלה של Person, לחיצה ימנית ו- Import->Export Data
![image](Stage1/mockData/2.jpeg)
 - תוצאת השאילתא `;SELECT * FROM Person`:
![image](Stage1/mockData/3.jpeg)
   

### כלי שני: שימוש ב-[generatedata](https://generatedata.com/generator) ליצירת קובץ CSV  
##### הזנת נתונים לטבלת Room  
- טווח מספרי קבוצה: 1-400  
📜 [צפייה ב-`Room.csv`](Stage1/genData/Room.csv)
##### הזנת נתונים לטבלת Class  
- טווח מספרי קבוצה: 1-400  
📜 [צפייה ב-`Class.csv`](Stage1/genData/Class.csv)
##### הזנת נתונים לטבלת ClassType  
- טווח מספרי קבוצה: 1-400  
📜 [צפייה ב-`ClassType.csv`](Stage1/genData/ClassType.csv)  

### דוגמה להמחשת העבודה באתר עבור הטבלה ClassType: 
- הגדרת סוגי תכונות הישות ושמותיהם באתר

![image](Stage1/genData/1.jpeg)

- עריכת ההגדרות להוצאת קובץ בפורמט CSV


![image](Stage1/genData/2.jpeg)

![image](Stage1/genData/3.jpeg)


- יצירת 400 רשומות לטבלה ולחיצה על Generate
  
![image](Stage1/genData/4.jpeg)


- העלאת הקובץ הנוצר למאגר וקבלת האישור להלן

![image](Stage1/genData/5.jpeg)

 - תוצאת השאילתה `;SELECT 'ClassType' AS table_name, COUNT(*) FROM ClassType`:

![image](Stage1/genData/6.jpeg)


#### כלי שלישי: שימוש ב-Python ליצירת קבצי CSV
##### יצירת נתונים לטבלת Equipment
- טווח מספרי קבוצה: 1-400  
📜 [צפייה ב-`Equipment.csv`](Stage1/pythonData/Equipment.csv)
##### יצירת נתונים לטבלת Certified_For  
- שני מפחתות זרים ע"פ טווחיהם
📜 [צפייה ב-`Certified_For.csv`](Stage1/pythonData/Certified_For.csv)
##### יצירת נתונים לטבלת Registers_For  
- שני מפתחות זרים ע"פ טווחיהם  
📜 [צפייה ב-`Registers_For.csv`](Stage1/pythonData/Registers_For.csv)

##### סקריפט היצירה: [צפייה ב-`genCSV.py`](Stage1/pythonData/genCSV.py)
- 3 קבצי הCSV שהסקריפט יצר הועלאו בהצלחה למאגר

![image](Stage1/pythonData/1.jpeg)

![image](Stage1/pythonData/2.jpeg)

![image](Stage1/pythonData/3.jpeg)


### גיבוי  
- קבצי הגיבוי נשמרים עם התאריך והשעה של מועד הגיבוי:
  
📜 [צפייה בתיקיית הגיבויים-`Backups`](Stage1)

- הצד המגבה: עומד על המאגר, לחיצה ימנית ובוחר את האפשרות של Backup.
- יש לבחור בפורמט Tar ולקרא לקובץ בשם backup_dd_mm_yy_hh_mi למען הסדר הטוב.
 


![1](https://github.com/user-attachments/assets/5319fd11-2a44-436d-9854-ab3b31784da2)


- הצד המשחזר: דואג שקובץ הגיבוי שנוצר יהיה נמצא אצלו בStorage Manager, עומד על המאגר, לחיצה ימנית ובוחר את האפשרות של Restore
- ובוחר את קובץ הגיבוי המדובר
  
![2](https://github.com/user-attachments/assets/b0399c59-ba81-4cc5-8699-3ca952d856ef)


## שלב 2: אינטגרציה ושאילתות
### שאילתות 
📜 [צפייה בקובץ השאילתות-`Queries.sql`](Stage2)

#### 8 שאילתות SELECT:
1. 

### אילוצים

📜 [צפייה בקובץ האילוצים-`Constraints.sql`](Stage2)


### אילוץ 1 על הטבלה - Room 
**תיאור השינוי:**
הוספנו אילוץ שבודק שקיבולת חדר היא ערך חיובי ולא גדולה מ-200.

**פקודת ALTER TABLE:**
```sql
ALTER TABLE Room
ADD CONSTRAINT chk_capacity_positive CHECK (Capacity > 0 AND Capacity <= 200);
```

**ניסיון להכניס נתון לא חוקי:**
```sql
INSERT INTO Room (IdR, NameR, Capacity)
VALUES (402, 'SmallRoom', 0);
```

**מה יקרה:**
שגיאה — האילוץ `chk_capacity_positive` יופעל ותתקבל הודעה:

![WhatsApp Image 2025-04-27 at 19 02 56](https://github.com/user-attachments/assets/61569dc4-e935-432e-8c2d-b011357fd29d)


---

### אילוץ 2 על הטבלה - Equipment 
**תיאור השינוי:**
שינינו את עמודת `Condition` כך שאם לא יוזן ערך — יוגדר אוטומטית כ-'T' (תקין).

**פקודת ALTER TABLE:**
```sql
ALTER TABLE Equipment
ALTER COLUMN Condition SET DEFAULT 'T';
```

**ניסיון להכניס ציוד בלי לציין Condition:**
```sql
INSERT INTO Equipment (IdE, NameE, IdR)
VALUES (201, 'Treadmill', 1);
```

**מה יקרה:**

לא תהיה שגיאה! 
![WhatsApp Image 2025-04-27 at 19 19 01](https://github.com/user-attachments/assets/600b64e1-6afa-4ea4-8e76-bb8e7d73f27b)

פשוט יתווסף לרשומה ערך ברירת מחדל `Condition = 'T'`.

תוצאת השאילתא ` ;SELECT * FROM Equipment WHERE IdE = 402` :

![WhatsApp Image 2025-04-27 at 19 41 32](https://github.com/user-attachments/assets/b8435748-ab4b-4342-8eae-e306b5bcc2c4)

---

### אילוץ 3 על הטבלה - Member
**תיאור השינוי:**
נוסף אילוץ שבודק ש-`ExpirationDate` גדול מ-`RegistrationDate`.

**פקודת ALTER TABLE:**
```sql
ALTER TABLE Member
ADD CONSTRAINT chk_member_dates CHECK (ExpirationDate > RegistrationDate);
```

**ניסיון להכניס נתון לא חוקי:**
```sql
INSERT INTO Member (Id, RegistrationDate, ExpirationDate)
VALUES (402, '2025-05-01', '2025-04-01');
```

**מה יקרה:**
תתקבל שגיאה על הפרת האילוץ:


![WhatsApp Image 2025-04-27 at 19 44 59](https://github.com/user-attachments/assets/f57b0240-2d5e-4451-8265-81e35cef354e)


