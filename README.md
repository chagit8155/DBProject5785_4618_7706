# DBProject5785_4618_7706

## תוכן עניינים  
- [שלב 1: תכנון ובניית מסד הנתונים](#שלב-1-תכנון-ובניית-מסד-הנתונים)  
  - [מבוא](#מבוא)  
  - [ERD (תרשים ישויות-קשרים)](#erd-תרשים-ישויות-קשרים)  
  - [DSD (תרשים מבנה נתונים)](#dsd-תרשים-מבנה-נתונים)  
  - [סקריפטים ב-SQL](#סקריפטים-ב-sql)  
  - [נתונים](#נתונים)  
  - [גיבוי](#גיבוי)  
- [שלב 2: שאילתות ואילוצים](#שלב-2-שאילתות-ואילוצים)
  - [שאילתות SELECT](#שאילתות-SELECT)
  - [שאילתות DELETE](#שאילתות-DELETE)
  - [שאילתות UPDATE](#שאילתות-UPDATE)
  - [אילוצים](#אילוצים)
  - [ביצוע Rollback וCommit ](#ביצוע-rollbac-ו-commit )
  - [גיבוי מעודכן](#גיבוי-מעודכן)
- [שלב 3: אינטגרציה ומבטים](#שלב-3-אינטגרציה-ומבטים)
  - [מבוא](#מבוא)
  - [תרשים DSD של המערכת החדשה](#תרשים-DSD-של-המערכת-החדשה)
  - [תהליך הנדסה הפוכה (Reverse Engineering)](#תהליך-הנדסה-הפוכה) 
  - [תרשים ERD של המערכת החדשה](#תרשים-ERD-של-המערכת-החדשה)
  - [ניתוח והשוואת המערכות](#ניתוח-והשוואת-המערכות)
  - [תהליך האינטגרציה](#תהליך-האינטגרציה)
  - [תרשים ERD משולב](#תרשים-ERD-משולב)
  - [החלטות אינטגרציה](#החלטות-אינטגרציה)
  - [תהליך מיפוי הנתונים](#תהליך-מיפוי-הנתונים)
  - [הסבר הפקודות SQL](#הסבר-הפקודות-sql)
  - [אתגרים ופתרונות](#אתגרים-ופתרונות)
  - [מסקנות](#מסקנות)


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
### שאילתות SELECT
📜 [צפייה בקובץ כל השאילתות-`Queries.sql`](Stage2)

#### שאילתה 1
**תיאור:**
השאילתה מחזירה את כל המדריכים (trainers) שהם גברים. היא מציגה את תעודת הזהות שלהם, שם, גיל ורמת ניסיון. התוצאה ממויינת לפי רמת הניסיון בסדר עולה ומיון משני לפי שם בסדר אלפביתי.

**השאילתה רצה בהצלחה:**

![WhatsApp Image 2025-04-28 at 02 44 08](https://github.com/user-attachments/assets/5f5dec79-6b7e-4a87-ab93-dc5307512d2a)


**צילום תוצאת השאילתה:**

![WhatsApp Image 2025-04-28 at 02 44 42](https://github.com/user-attachments/assets/a6b5ab5e-ce04-47fe-9ec8-ded0c93f2ae5)

---

#### שאילתה 2
**תיאור:**
השאילתה מחזירה את מספר השיעורים שכל מדריך מלמד, יחד עם שמו. התוצאות ממויינות לפי כמות השיעורים בסדר יורד.

**השאילתה רצה בהצלחה:**

![WhatsApp Image 2025-04-28 at 02 56 14](https://github.com/user-attachments/assets/6cd9c263-2f27-4a17-bd28-d36cddff4984)


**צילום תוצאת השאילתה:**

![WhatsApp Image 2025-04-28 at 02 56 43](https://github.com/user-attachments/assets/a1f47a12-da63-4fcb-a513-12661c1664f7)

---

#### שאילתה 3
**תיאור:**
השאילתה מציגה את רשימת המנויים שהמנוי שלהם יפוג בחודש הבא, כולל שם המנוי ותאריך התפוגה. התוצאות ממויינות לפי תאריך התפוגה בסדר עולה.

**הרצת השאילתה:**

![WhatsApp Image 2025-04-28 at 03 05 32](https://github.com/user-attachments/assets/497771e1-4532-4247-a884-88f59a434849)



**צילום תוצאת השאילתה:**

![WhatsApp Image 2025-04-28 at 03 05 49](https://github.com/user-attachments/assets/fd4f8847-51b5-47fa-bcc9-f821ff68ff44)

---

#### שאילתה 4
**תיאור:**
השאילתה מציגה את פרטי השיעורים שמתקיימים היום: יום בשבוע, מזהה שיעור, שעה, סוג שיעור, מזהה המדריך, רמת הניסיון של המדריך ושם החדר.

**הרצת השאילתה:**

![WhatsApp Image 2025-04-28 at 03 08 48](https://github.com/user-attachments/assets/0c8d86b4-4f1d-4578-8f0d-1a24876ed827)


**צילום תוצאת השאילתה:**

![WhatsApp Image 2025-04-28 at 03 09 44](https://github.com/user-attachments/assets/44323c1f-7e7a-4230-9736-f6a01dcafe18)



---

#### שאילתה 5
**תיאור:**
השאילתה מציגה את כל השיעורים אליהם מנוי בעל מזהה 1 רשום, כולל שם המנוי, מזהה השיעור, סוג השיעור, יום בשבוע, שעה ושם החדר.

**הרצת השאילתה:**

![WhatsApp Image 2025-04-28 at 03 21 03](https://github.com/user-attachments/assets/df75567d-91bf-41c6-a963-ad6b9e3df9f3)


**תוצאת השאילתה:**

![WhatsApp Image 2025-04-28 at 03 21 21](https://github.com/user-attachments/assets/875146a8-7145-45ba-9bfe-1887edd48031)

---

#### שאילתה 6
**תיאור:**
השאילתה מציגה את פרטי החדרים הפנויים היום (חדרים שלא מתקיים בהם שיעור), כולל מזהה החדר, שם החדר ותכולת החדר. התוצאות ממויינות לפי שם החדר.

**הרצת השאילתה:**

![WhatsApp Image 2025-04-28 at 03 23 56](https://github.com/user-attachments/assets/1321a298-869c-406a-8944-30cefac72d54)



**תוצאת השאילתה:**

![WhatsApp Image 2025-04-28 at 03 24 27](https://github.com/user-attachments/assets/79adb7d3-709a-4e78-b05d-5f77504f8e31)

---

#### שאילתה 7
**תיאור:**
השאילתה מציגה את פרטי המנויים שרשומים לשיעור מסויים (מזהה שיעור 5). מוצגים תעודת זהות, שם, מגדר ותאריך לידה של כל מנוי.


**הרצת השאילתה:**

![WhatsApp Image 2025-04-28 at 03 31 58](https://github.com/user-attachments/assets/ef5effa7-f2ba-41b1-9ddf-84c9d02983ed)

**תוצאת השאילתה:**

![WhatsApp Image 2025-04-28 at 03 32 17](https://github.com/user-attachments/assets/791caa5f-4871-4950-baa7-69ce7430d189)

---

#### שאילתה 8
**תיאור:**
השאילתה מציגה את כל השיעורים שהגבלת גיל המינימלית שלהם מתאימה לגיל 19 (כלומר, המינימום הוא 19 או פחות). מוצגים מזהה שיעור, יום בשבוע, שעה, סוג שיעור, גיל מינימלי נדרש ושם החדר.

**הרצת השאילתה:**

![WhatsApp Image 2025-04-28 at 03 34 05](https://github.com/user-attachments/assets/0ff2f21e-5f0c-4850-bc92-bf1a6354e951)


**תוצאת השאילתה:**
![WhatsApp Image 2025-04-28 at 03 34 18](https://github.com/user-attachments/assets/5da9be7b-598a-4dd4-a5f1-a502a51b8dd7)

---

### שאילתות DELETE
#### 🔻 שאילתה 1 – מחיקת מדריכים בעלי ניסיון נמוך שלא מעבירים שיעורים

**תיאור:**  
בשאילתה זו נמחקים מדריכים (Trainer) בעלי רמת ניסיון 1, אשר אינם משויכים לאף שיעור בטבלה `Class`. כלומר, מדריכים חסרי ניסיון שלא מעבירים בפועל שיעורים.
השאילתה משתמשת בתנאי `NOT IN` יחד עם שאילתה פנימית הבודקת אילו מדריכים מופיעים בטבלת השיעורים.
**צילום הרצה:**

![WhatsApp Image 2025-05-05 at 03 02 06](https://github.com/user-attachments/assets/1db9e862-f1ee-4a3b-86ca-bde6c8e973e2)
 

**צילום לפני:**  

![WhatsApp Image 2025-05-05 at 03 04 28](https://github.com/user-attachments/assets/3e617424-6b2a-4867-b9d0-35d519be6b22)



תוכן טבלת `Trainer` כולל מדריכים עם ניסיון 1, שלא נמצאים בטבלת `Class`.


**צילום אחרי:**  

![WhatsApp Image 2025-05-05 at 03 03 48](https://github.com/user-attachments/assets/1eb535a9-df54-4082-8b78-82da8d0d1ddc)


אותם מדריכים נמחקים מהטבלה לאחר ההרצה.

---

#### 🔻 שאילתה 2 – מחיקת מנויים שפג תוקפם והם מעל גיל 30

**תיאור:**  
בשאילתה זו נמחקים מנויים (`Member`) אשר תוקף המנוי שלהם פג לפני יותר משנה, וגם גילם מעל 30.
לשם כך נעשה שימוש בשתי טבלאות – `Member` ו־`Person`: תנאי הגיל נבדק על פי שדה `DateOfBirth` בטבלת `Person`.
**צילום הרצה:** 

![WhatsApp Image 2025-05-05 at 03 05 41](https://github.com/user-attachments/assets/1c2a32ea-46dc-4190-9950-db925457b555)

**צילום לפני:**  

![WhatsApp Image 2025-05-05 at 03 07 07](https://github.com/user-attachments/assets/587ebe03-0527-4d3e-b9b4-e1223e0a72cd)


טבלת `Member` כוללת מנויים שתוקף המנוי שלהם פג.  
טבלת `Person` מראה כי הם מעל גיל 30.

**צילום אחרי:**  

![WhatsApp Image 2025-05-05 at 03 06 39](https://github.com/user-attachments/assets/21a1886e-f6fa-444c-85c5-6eaf21b36e01)


אותם מנויים נמחקים מטבלת `Member`.

---

#### 🔻 שאילתה 3 – מחיקת שיעורים שלא נרשמו אליהם מנויים בשנתיים האחרונות

**תיאור:**  
בשאילתה זו נמחקים שיעורים (`Class`) שאליהם לא נרשמו מנויים בשנתיים האחרונות.  
מבוצעת בדיקה מול טבלת `registers_for`, תוך שימוש ב־`JOIN` לטבלת `Member` כדי לבדוק תאריך הרשמה של המנוי.
**צילום הרצה:** 
![WhatsApp Image 2025-05-05 at 03 08 07](https://github.com/user-attachments/assets/a8c6affb-199e-4503-a95b-e89d87a72432)


**צילום לפני:**  
![WhatsApp Image 2025-05-05 at 03 09 25](https://github.com/user-attachments/assets/54fdec2a-5514-4227-a023-82987f6f73d8)


טבלת `Class` כוללת שיעורים, וחלקם לא נרשמו אליהם כלל בשנתיים האחרונות.

**צילום אחרי:** 
![WhatsApp Image 2025-05-05 at 03 08 43](https://github.com/user-attachments/assets/88fce717-2bb5-45d1-b597-769755b7b51b)


השיעורים האלו הוסרו מהטבלה לאחר ההרצה.




### שאילתות UPDATE

#### ❖ שאילתה 1 – הארכת מנוי לחברים ותיקים

**תיאור:**
השאילתה מזההה את המנויים שבין תאריך הרשמה לתאריך פקעהם המנוי עברו למעלה משנתיים (730 ימים ≈ 2 שנים). מנויים אלה מקבלים "מתנה" – הארכת המנוי בחודשיים.

**צילום הרצת השאילתה:**


![WhatsApp Image 2025-05-05 at 12 48 42](https://github.com/user-attachments/assets/2f085b6f-f924-4e84-b533-3c013c9ef8c0)

```sql
SELECT *
FROM Member
WHERE ExpirationDate - RegistrationDate > 365;
```

**לפני העדכון:**
(צילום המסך יראה את תאריכי RegistrationDate ו‏ExpirationDate של המנויים רלוונטיים)

![WhatsApp Image 2025-05-05 at 12 53 41](https://github.com/user-attachments/assets/db911099-a748-4f28-a49d-0747a0257cbd)



**אחרי העדכון:**
(צילום מסך נוסף של אותה השאילתה – הצוג של‏ExpirationDate הוצא חודשיים קדימה)

![WhatsApp Image 2025-05-05 at 12 52 46](https://github.com/user-attachments/assets/3ec2f919-17ef-4068-a4c4-195f3c7de520)


---

#### ❖ שאילתה 2 – קידום מדריכים על סמך פעילות

**תיאור:**
השאילתה מזההה מדריכים שהעבירו למעלה מי-100 שיעורים בשנה האחרונה. למדריכים אלה תעלה רמת הניסיון בעד דרגה אחת, עד למקסימום של דרגה 3.

**הרצת השאילתה:**

![WhatsApp Image 2025-05-05 at 18 31 45](https://github.com/user-attachments/assets/11b213d9-7c95-4d0c-be14-8f83d9289b7f)


**תוצאות השאילתה:**

```sql
SELECT
  T.Id,
  T.ExperienceLevel AS current_experience,
  LEAST(T.ExperienceLevel + 1, 3) AS new_experience
FROM Trainer T
WHERE T.Id IN (
  SELECT Id
  FROM Class
  GROUP BY Id
  HAVING COUNT(*) * 4 * 12 >= 100
);
```

**לפני העדכון:**
(צילום שמרא את ExperienceLevel הנוכחי ואת הדרגה החדשה)

![WhatsApp Image 2025-05-05 at 13 20 08](https://github.com/user-attachments/assets/bd8fca6a-06b7-42d0-b398-f2203c095981)


**אחרי העדכון:**
(צילום חוזר – שמרא שהדרגה עודכנה)

![WhatsApp Image 2025-05-05 at 13 19 31](https://github.com/user-attachments/assets/24d21797-cb31-4d6e-aaec-cc774c892867)




---

#### ❖ שאילתה 3 – החלפת ציוד תקול בציוד תקין אחר

**תיאור:**
השאילתה מחליפה ציוד תקול (בעל מזהה IdE = 58) בציוד תקין אחר שבעל אותו שם (NameE) ושאינו משובץ לאף חדר (כלמש IdR IS NULL). הציוד החלופי משויך לחדר שאליו שייך הציוד התקול.

**הרצת השאילתה:**

![WhatsApp Image 2025-05-05 at 14 29 45](https://github.com/user-attachments/assets/c71a45d8-3616-457b-a44e-2125d17076d4)

**תוצאת השאילתה:**

```sql
SELECT *
FROM Equipment
WHERE IdE = 11 OR IdE = 58;
```

**לפני העדכון:**
(צילום שבו ניתן לראות את הציוד התקול IdE = 58 ואת הציוד החלופי IdE = 11 עם IdR = NULL)

![WhatsApp Image 2025-05-05 at 14 28 58](https://github.com/user-attachments/assets/2089cf2a-e04e-4efb-ad2b-2b129b3ff7b9)


**אחרי העדכון:**
(צילום שמרא שציוד 11 עודכן כי IdR שלו זהה ל-IdR של ציוד 58)
![WhatsApp Image 2025-05-05 at 14 30 21](https://github.com/user-attachments/assets/4b5dc4bb-fbf7-4865-9a4a-52341e70953e)




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


### ביצוע Rollback וCommit

📜 [צפייה בקוד-`RollbackCommit.sql`](Stage2)

#### ביצוע עדכון עם ROLLBACK

#### 1. הצגת מצב טבלת Room לפני העדכון:
ביצענו שאילתה להצגת כלל הרשומות בטבלת Room. בשלב זה ניתן לראות את המצב המקורי של החדרים בבסיס הנתונים, לפני כל שינוי.


![WhatsApp Image 2025-04-28 at 11 54 21](https://github.com/user-attachments/assets/776e5f7f-03d6-4f26-be92-f4aa26788503)



#### 2. ביצוע עדכון:
עדכנו את שם החדר בעל המזהה IdR = 1 ל- 'BeforeRollback'.

#### 3. הצגת מצב טבלת Room לאחר העדכון:

![WhatsApp Image 2025-04-28 at 03 44 11](https://github.com/user-attachments/assets/c877402f-a937-4641-b578-1cc80cd1f95b)


בשלב זה, לאחר ביצוע פקודת העדכון, שם החדר עם מזהה 1 השתנה ל- 'BeforeRollback'. עם זאת, מאחר שטרנזקציה זו טרם בוצעה COMMIT, העדכון עדיין לא נשמר לצמיתות בבסיס הנתונים.

#### 4. ביצוע ROLLBACK:
הפעלנו את פקודת ROLLBACK, אשר מבטלת את כל השינויים שבוצעו מאז תחילת הטרנזקציה. בכך חזר בסיס הנתונים למצבו הקודם.

#### 5. הצגת מצב טבלת Room לאחר ה-ROLLBACK:
ביצענו שוב שאילתה להצגת תוכן הטבלה. ניתן לראות שהשינוי שבוצע התבטל והמידע בטבלה חזר להיות כפי שהיה לפני העדכון.

![WhatsApp Image 2025-04-28 at 03 47 08](https://github.com/user-attachments/assets/31a4be2b-2a55-4cc7-af7f-9c264f15c520)


---

#### ביצוע עדכון עם COMMIT

#### 1. הצגת מצב טבלת Room לפני העדכון:
ביצענו שוב שאילתה להצגת תוכן הטבלה, לוודא שאנו מתחילים מהמצב העדכני והמקורי לאחר ה-ROLLBACK.

![WhatsApp Image 2025-04-28 at 12 23 15](https://github.com/user-attachments/assets/52bbcfa6-d852-4aa7-afe5-9d718e764356)


#### 2. ביצוע עדכון:
ביצענו עדכון נוסף על טבלת Room, הפעם שינינו את קיבולת החדר בעל מזהה IdR = 1 ל- 45.

#### 3. הצגת מצב טבלת Room לאחר העדכון:
לאחר העדכון, הקובלת אכן השתנתה ל-45. השינוי עדיין זמני עד ביצוע COMMIT.


![WhatsApp Image 2025-04-28 at 12 36 04](https://github.com/user-attachments/assets/528df950-c1c4-40af-aaba-171d9f02d813)



#### 4. ביצוע COMMIT:
הרצנו את פקודת COMMIT, אשר מאשרת את כל השינויים שבוצעו בטרנזקציה ומבצעת אותם לצמיתות בבסיס הנתונים.

#### 5. הצגת מצב טבלת Room לאחר ה-COMMIT:
לאחר ביצוע ה-COMMIT, בצענו שוב שאילתה על הטבלה וראינו כי קיבלת החדר עודכנה ל- 45 באופן קבוע.

![WhatsApp Image 2025-04-28 at 12 41 33](https://github.com/user-attachments/assets/f24b2b5e-0e2e-4f43-afb7-5a4a6a3d9990)





### גיבוי מעודכן

📜 [צפייה בקוד-`backup_05_05_25_18_19`](Stage2)



## שלב 3: אינטגרציה ומבטים
---

### מבוא

במסגרת שלב ג' של הפרויקט, ביצענו אינטגרציה של שני מערכות בסיסי נתונים עצמאיות:
- **מערכת מקורית**: מערכת ניהול מכון כושר
- **מערכת חדשה**: מערכת ניהול חוגי ספורט

המטרה: ליצור מערכת משולבת אחת המכילה את כל הפונקציונליות של שתי המערכות, תוך שמירה על תקינות הנתונים והיחסים ביניהם.

---
### תרשים DSD של המערכת החדשה (חוגי ספורט)
![DSDSportClasses](https://github.com/user-attachments/assets/5e12ef0b-c928-4dd9-a149-41bd2b7228c3)


### תהליך הנדסה הפוכה (Reverse Engineering)


### שלב 1: יצירת DSD מגיבוי המס"ד שקיבלנו

מתוך הקובץ `CreateTables.sql`  ומה-DSD שיתווצרו אוטומטית מהגיבוי, זיהינו את הטבלאות הבאות:

#### טבלאות הליבה:
- **person**: מכילה פרטי אנשים בסיסיים
- **course**: מכילה פרטי קורסים
- **studio**: מכילה פרטי אולמות
- **timeslot**: מכילה זמני השיעורים
- **equipment**: מכילה פרטי ציוד

#### טבלאות התמחות:
- **participant**: יורשת מ-person (מתאמנים)
- **trainer**: יורשת מ-person (מדריכים)

#### טבלאות קישור:
- **class**: שיעור (ישות חלשה)
- **enrolled**: רישום למשתתפים
- **require**: דרישות ציוד לקורסים

### שלב 2: זיהוי סוגי הישויות

#### ישויות רגילות:
```sql
-- מזוהות על פי מפתח ראשי פשוט
person: PRIMARY KEY (person_id)
course: PRIMARY KEY (course_id)
studio: PRIMARY KEY (studio_id)
timeslot: PRIMARY KEY (timeslot_id)
equipment: PRIMARY KEY (eq_id)
```

#### ישות חלשה:
```sql
-- מזוהית על פי מפתח ראשי מורכב ממפתחות זרים
class: PRIMARY KEY (timeslot_id, studio_id)
```

**הסבר למה Class היא ישות חלשה:**
1. המפתח הראשי מורכב משני מפתחות זרים
2. אין מזהה עצמאי לשיעור
3. קיום השיעור תלוי במקום ובזמן
4. לא יכול להיות שיעור ללא timeslot ו-studio

##### יחסי הכללה (ISA):
```sql
-- מזוהים כאשר המפתח הראשי הוא גם מפתח זר
participant: PRIMARY KEY (person_id) + FOREIGN KEY → person
trainer: PRIMARY KEY (person_id) + FOREIGN KEY → person
```

#### שלב 3: זיהוי יחסים

##### יחסי 1:N:
- **course → class**: קורס אחד יכול להיות בכמה שיעורים
- **trainer → class**: מדריך אחד יכול ללמד כמה שיעורים
- **timeslot → class**: זמן אחד יכול לכלול כמה שיעורים (באולמות שונים)
- **studio → class**: אולם אחד יכול לארח כמה שיעורים (בזמנים שונים)

##### יחסי M:N:
- **participant ↔ class** (דרך enrolled): מתאמן יכול להירשם לכמה שיעורים, שיעור יכול לכלול כמה מתאמנים
- **course ↔ equipment** (דרך require): קורס יכול לדרוש כמה ציודים, ציוד יכול לשמש כמה קורסים

---

### תרשים ERD של המערכת החדשה
![sportClassesERD](https://github.com/user-attachments/assets/f8c409a7-d4ef-43f2-a964-3ee19926da08)

---

### ניתוח והשוואת המערכות

#### מערכת מקורית (מכון כושר):
**ישויות עיקריות:**
- Person (בסיס)
- Member, Trainer (התמחויות)
- ClassType (סוגי שיעורים)
- Room (חדרים)
- Equipment (ציוד)
- Class (שיעורים)

**מאפיינים:**
- מכוון לניהול חברות
- דגש על חדרים פיזיים
- מערכת סיווג פשוטה של שיעורים

#### מערכת חדשה (שיעורי ספורט):
**ישויות עיקריות:**
- Person (בסיס)
- Participant, Trainer (התמחויות)
- Course (קורסים מפורטים)
- Studio (אולמות)
- TimeSlot (זמנים מובנים)
- Equipment (ציוד מתקדם)
- Class (שיעורים מורכבים)

**מאפיינים:**
- מכוון למגוון פעילויות ספורט
- דגש על תזמון מדויק
- מערכת מחירים מפורטת
- הגבלות גיל מתקדמות

---

## תרשים ERD משולב
![IntegrationERD](https://github.com/user-attachments/assets/bdc65ebc-f68d-498f-9716-2edd91a965b0)


## תהליך האינטגרציה

### שלב 1: זיהוי נקודות המפגש

**ישויות זהות:**
- Person ↔ Person
- Member ↔ Participant
- Trainer ↔ Trainer
- Equipment ↔ Equipment
- Class ↔ Class

**ישויות דומות:**
- ClassType ↔ Course
- Room ↔ Studio
- (חסר) ↔ TimeSlot

#### שלב 2: החלטות מיזוג

##### החלטה 1: מיזוג Person
**בעיה:** שתי המערכות מכילות טבלת Person עם שדות שונים
**פתרון:** השלמת השדות החסרים
```sql
-- הוספת שדות חסרים למערכת המקורית
ALTER TABLE Person ADD COLUMN email VARCHAR(100);
ALTER TABLE Person ADD COLUMN phone VARCHAR(20);
```

##### החלטה 2: איחוד ClassType ו-Course
**בעיה:** שתי מערכות שונות לתיאור סוגי שיעורים
**פתרון:** יצירת טבלת Course מאוחדת עם כל השדות הנדרשים
```sql
CREATE TABLE Course (
    course_id integer,
    course_name VARCHAR(50),
    required_experience NUMERIC(1,0),
    min_age NUMERIC(2,0),
    price NUMERIC(6,2),
    PRIMARY KEY (course_id)
);
```

##### החלטה 3: יצירת TimeSlot
**בעיה:** המערכת המקורית לא מכילה ניהול זמנים מובנה
**פתרון:** יצירת טבלת TimeSlot חדשה ומיפוי הנתונים הקיימים
```sql
CREATE TABLE TimeSlot (
    timeslot_id integer,
    day character varying(15),
    start_time character varying(15),
    end_time character varying(15),
    PRIMARY KEY (timeslot_id)
);
```

##### החלטה 4: איחוד Room ו-Studio
**בעיה:** שתי מערכות למיקומים פיזיים
**פתרון:** שמירה על שתי הטבלאות עם קשר ביניהן - בתוך סטודיו/מכון יש כמה חדרים
- Room - חדרים פיזיים
- Studio - מקומות מושגיים עם מיקום

---

#### תהליך מיפוי הנתונים

#### מיפוי מזהים
כדי למנוע התנגשויות במזהים, השתמשנו בהסטה:
```sql
-- מזהי אנשים: +1000
INSERT INTO Person (person_id, ...)
SELECT (person_id + 1000), ...
FROM person_remote;

-- מזהי קורסים: +1000
INSERT INTO Course (course_id, ...)
SELECT (course_id + 1000), ...
FROM course_remote;

-- מזהי ציוד: +1000
INSERT INTO Equipment (eq_id, ...)
SELECT (eq_id + 1000), ...
FROM equipment_remote;
```

#### מיפוי נתונים חסרים
```sql
-- השלמת אימיילים וטלפונים אקראיים
UPDATE Person
SET email = LOWER(SUBSTRING(REPLACE(person_name, ' ', ''), 1, 5)) 
           || FLOOR(random()*10000)::int || '@gmail.com',
    phone = '05' || FLOOR(random()*100000000)::int
WHERE email IS NULL OR phone IS NULL;
```

#### יצירת קשרים חדשים
```sql
-- קישור שיעורים לזמנים חדשים
UPDATE Class c
SET timeslot_id = t.timeslot_id
FROM TimeSlot t
WHERE c.DayInWeek = t.day
  AND TO_CHAR(TO_TIMESTAMP(t.start_time, 'HH24:MI'), 'HH24') = LPAD(c.HourC, 2, '0');
```

---

### הסבר הפקודות SQL

#### שלב 1: הכנת הסביבה
```sql
-- יצירת חיבור למסד הנתונים המרוחק
CREATE EXTENSION IF NOT EXISTS postgres_fdw;
CREATE SERVER sportclasses_server
FOREIGN DATA WRAPPER postgres_fdw
OPTIONS (host 'localhost', dbname 'sport', port '5432');
```

**הסבר:** יצירת תשתית לחיבור בין שני מסדי נתונים באמצעות Foreign Data Wrapper.

#### שלב 2: יצירת טבלאות זרות
```sql
CREATE FOREIGN TABLE person_remote (
    person_id integer,
    person_name character varying(80),
    -- שאר השדות...
) SERVER sportclasses_server
OPTIONS (schema_name 'public', table_name 'person');
```

**הסבר:** יצירת "חלונות" לטבלאות במסד הנתונים המרוחק, המאפשרות קריאה ישירה מהטבלאות המקוריות.

#### שלב 3: הכנת המבנה
```sql
-- הסרת אילוצים לפני שינויים
ALTER TABLE registers_for DROP CONSTRAINT registers_for_pkey;

-- שינוי סוגי נתונים
ALTER TABLE Person ALTER COLUMN Id TYPE INTEGER;

-- החזרת אילוצים
ALTER TABLE Person ADD PRIMARY KEY (Id);
```

**הסבר:** תהליך מבוקר של שינוי מבנה הטבלאות תוך שמירה על תקינות הנתונים.

#### שלב 4: העברת נתונים
```sql
INSERT INTO Person (person_id, person_name, Gender, birth_date, email, phone)
SELECT 
    (person_id + 1000), 
    person_name, 
    CASE 
        WHEN LOWER(gender) = 'male' THEN 'M'
        WHEN LOWER(gender) = 'female' THEN 'F'
        ELSE NULL
    END,
    birth_date, 
    email, 
    phone
FROM person_remote
WHERE (person_id + 1000) NOT IN (SELECT person_id FROM Person);
```

**הסבר:** העברת נתונים עם התאמות:
- הסטת מזהים למניעת התנגשויות
- המרת ערכי מגדר לפורמט אחיד
- בדיקת קיום למניעת כפילויות

---

### אתגרים ופתרונות

#### אתגר 1: התנגשות מזהים
**בעיה:** שני מסדי הנתונים משתמשים באותם מזהים
**פתרון:** הסטה קבועה של 1000 למזהי המערכת החדשה

#### אתגר 2: פורמטים שונים של נתונים
**בעיה:** המערכות משתמשות בפורמטים שונים (M/F vs Male/Female)
**פתרון:** פונקציות המרה עם CASE statements

#### אתגר 3: שדות חסרים
**בעיה:** טבלאות דומות עם שדות שונים
**פתרון:** הוספת שדות חסרים עם ערכי ברירת מחדל או ערכים אקראיים

#### אתגר 4: יחסים מורכבים
**בעיה:** מבני יחסים שונים בין המערכות
**פתרון:** יצירת טבלאות אמצע והתאמת הקשרים

#### אתגר 5: תלות בזמן
**בעיה:** המערכת המקורית לא מכילה מבנה זמנים מובנה
**פתרון:** יצירת TimeSlot חדש ומיפוי מהשדות הקיימים

---

### מסקנות

#### הישגים עיקריים:
1. **אינטגרציה מוצלחת** של שתי מערכות מורכבות
2. **שמירה על תקינות הנתונים** לאורך כל התהליך
3. **יצירת מערכת מאוחדת** עם יכולות משופרות
4. **פתרון בעיות תאימות** בין מערכות שונות

#### שיפורים שהושגו:
- **ניהול זמנים משופר** עם TimeSlot
- **מערכת מחירים מפורטת** מהמערכת החדשה
- **ניהול ציוד מתקדם** עם הגבלות גיל
- **גמישות רישום** עם אפשרויות מגוונות


המערכת המשולבת מספקת כעת פתרון מקיף לניהול מכוני כושר ולא מכון אחד, כלומר עם יכולת לנהל חוגי ספורט או עוד מכונים במיקומים שונים, תוך שמירה על כל הפונקציונליות המקורית של שתי המערכות.
