
# *Library Management Application*


#### Submitted By 
Chithra Sooryalayam Das - 10639842
G Mallikharjuna Rao     - 10638140
Pranav Dinesh Kumar     - 10625304
Haripriya Joshy         - 10637070

## *About*


(Built with Flask, MySQL)

## *Getting Started*

1. Install requirements
   sh
   pip install -r requirements.txt
   
2. Setup MySQL and replace host, user, password values in `setupDB.py`, `app.py` and `test.py` as required </br></br>
3. Create Database and Tables using `setupDB.py`
   sh
    cd utils
    python setupDB.py
    cd ..
   
4. Run app
   sh
   python app.py
   

## About the project 

We've created a robust library management system utilizing Flask and MySQL that empowers us, the librarians, to seamlessly handle various facets of our library operations. Our system consists of five core screens: Reports, Books, Members, Transactions, and Search. Each screen serves a specific purpose, contributing to an organized and efficient library management process.

#### Reports:
The Reports section offers us valuable insights, showcasing the highest paying customers and the most frequently rented books. This feature enables us to better understand user behavior and book preferences, assisting us in making informed decisions based on data.

#### Books:
In the Books section, we can manage our library's book inventory with ease. It provides functionalities that allow us to add, edit, and delete books. Our system ensures accurate data entry by guiding us through a robust validation process when adding new books, maintaining an up-to-date and well-maintained book collection.

#### Members:
Our Members section streamlines the management of library members. It provides us with tools to add new members, update their information, and remove members as needed. The comprehensive member information table displays key details, such as outstanding debts and total spending, providing us with a clear overview of each member's status.

#### Transactions:
Efficient book lending and returns are made possible through our Transactions section. We can easily lend books to members, specifying the per-day rental charges for each book. As books are borrowed, our system automatically updates the available quantity in our inventory. Upon return, the system calculates rental charges based on the borrowing duration and updates the inventory accordingly.

#### Search:
Our Search feature equips us with a powerful tool to quickly locate books by title or author. This functionality enhances the user experience and allows us to promptly assist library visitors in finding the books they're looking for.

To sum it up, our library management system, developed using Flask and MySQL, encompasses a range of essential features that optimize our library operations. From generating insightful reports to managing book inventory, members, and transactions, the system empowers us to efficiently and effectively manage our library. It enhances user experience, simplifies administrative tasks, and contributes to the overall efficiency of our library's day-to-day operations.


## *Screenshots:*

![1](https://user-images.githubusercontent.com/49085834/121894715-142b1900-cd3d-11eb-8e69-9b75cb96a6fe.png)
![2](https://user-images.githubusercontent.com/49085834/121894744-1db48100-cd3d-11eb-8025-470a3bf281a8.png)
![3](https://user-images.githubusercontent.com/49085834/121894765-23aa6200-cd3d-11eb-9424-6f0ce711c222.png)
![4](https://user-images.githubusercontent.com/49085834/121894850-3f156d00-cd3d-11eb-8c5d-f2206aab7e0a.png)
![10 6](https://user-images.githubusercontent.com/49085834/121895080-7a17a080-cd3d-11eb-899e-f2b55e6c5b1e.png)
![10 4](https://user-images.githubusercontent.com/49085834/121895357-c06cff80-cd3d-11eb-99f6-25a86a85dcea.png)
![Search](https://user-images.githubusercontent.com/49085834/121896734-40479980-cd3f-11eb-8e78-570c25801596.png)
![Report](https://user-images.githubusercontent.com/49085834/121896485-f8c10d80-cd3e-11eb-9ef9-c06db4ea6980.png)