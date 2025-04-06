# DBProject5785_4618_7706

## תוכן עניינים  
- [שלב 1: תכנון ובניית מסד הנתונים](#שלב-1-תכנון-ובניית-מסד-הנתונים)  
  - [מבוא](#מבוא)  
  - [ERD (תרשים ישויות-קשרים)](#erd-תרשים-ישויות-קשרים)  
  - [DSD (תרשים מבנה נתונים)](#dsd-תרשים-מבנה-נתונים)  
  - [סקריפטים ב-SQL](#סקריפטים-ב-sql)  
  - [נתונים](#נתונים)  
  - [גיבוי](#גיבוי)  
- [שלב 2: אינטגרציה](#שלב-2-אינטגרציה)  

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

 - תוצאת השאילתא `;SELECT 'ClassType' AS table_name, COUNT(*) FROM ClassType`:

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

# סקריפט היצירה: [צפייה ב-`genCSV.py`](Stage1/pythonData/genCSV.py)
- 3 קבצי הCSV שהסקריפט יצר הועלאו בהצלחה למאגר
![image](Stage1/pythonData/1.jpeg)

![image](Stage1/pythonData/2.jpeg)

![image](Stage1/pythonData/3.jpeg)


### גיבוי  
- קבצי הגיבוי נשמרים עם התאריך והשעה של מועד הגיבוי:




