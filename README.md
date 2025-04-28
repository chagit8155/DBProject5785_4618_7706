# DBProject5785_4618_7706

## תוכן עניינים  
- [שלב 1: תכנון ובניית מסד הנתונים](#שלב-1-תכנון-ובניית-מסד-הנתונים)  
  - [מבוא](#מבוא)  
  - [ERD (תרשים ישויות-קשרים)](#erd-תרשים-ישויות-קשרים)  
  - [DSD (תרשים מבנה נתונים)](#dsd-תרשים-מבנה-נתונים)  
  - [סקריפטים ב-SQL](#סקריפטים-ב-sql)  
  - [נתונים](#נתונים)  
  - [גיבוי](#גיבוי)  
- [שלב 2: שאילתות ואילוצים](#שלב-2-שאילתות ואילוצים)
  - [שאילתות SELECT](#שאילתות-SELECT)
  - [שאילתות DELETE](#שאילתות-DELETE)
  - [שאילתות UPDATE](#שאילתות-UPDATE)
  - [אילוצים](#אילוצים)
  - [ביצוע Rollback וCommit ](#ביצוע-rollbac-ו-commit )
  - [גיבוי מעודכן](#גיבוי-מעודכן)


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


### שאילתות UPDATE


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

### ביצוע Rollback ו Commit

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






















