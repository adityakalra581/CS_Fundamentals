# Class 12 Computer Science: SQL Test

**Time:** 30 minutes
**Maximum Marks:** 25

---

## Section A: Theory (12 marks)

Each question carries 2 marks.

**Q1.** Differentiate between a *primary key* and a *foreign key*. Give one example of each.

**Q2.** Differentiate between the `WHERE` clause and the `HAVING` clause.

**Q3.** Differentiate between `DELETE` and `DROP TABLE`.

**Q4.** Classify each of the following commands as DDL, DML or DQL:
`CREATE`, `INSERT`, `SELECT`, `ALTER`, `UPDATE`, `DROP`

**Q5.** A student writes the query below to find books whose quantity is not known, but it returns no rows even though such books exist.
```sql
SELECT Title FROM BOOK WHERE Qty = NULL;
```
Explain why this happens and write the correct query.

**Q6.** Differentiate between the data types `CHAR(10)` and `VARCHAR(10)`.

---

## Section B: Coding (13 marks)

Use the table **BOOK** given below for Q8 and Q9.

| BookID | Title | Author | Price | Qty | Category |
|---|---|---|---|---|---|
| 101 | Wings of Fire | A.P.J. Abdul Kalam | 250 | 10 | Biography |
| 102 | Python Basics | R. Sharma | 450 | 5 | Technology |
| 103 | The Alchemist | Paulo Coelho | 300 | 8 | Fiction |
| 104 | Database Systems | S. Gupta | 550 | 4 | Technology |
| 105 | Malgudi Days | R.K. Narayan | 200 | 12 | Fiction |
| 106 | Atomic Habits | James Clear | 400 | NULL | Self-Help |

**Q7.** (3 marks)
(a) Write a query to create the table `BOOK` with the following requirements:
- `BookID`: integer, primary key
- `Title`: text up to 50 characters, must not be empty (NOT NULL)
- `Author`: text up to 30 characters
- `Price`: decimal number with up to 5 digits before the decimal point and 2 after it
- `Qty`: integer, with a default value of 0
- `Category`: text up to 20 characters

(b) Write a query to insert the record of the book with BookID 101 (first row of the table above).

**Q8.** (4 marks) Write SQL queries for the following:
(a) Display the title and price of all books costing more than 300, with the costliest book first.
(b) Display the different categories of books, without repetition.
(c) Increase the price of all books in the "Fiction" category by 10%.
(d) Delete the record of the book whose BookID is 105.

**Q9.** (6 marks) Write SQL queries for the following:
(a) Display each category along with the number of books in it.
(b) Display each category along with the total quantity of its books, only for those categories whose total quantity is more than 10.
(c) Display the titles of all books whose quantity is not known (NULL).

---
