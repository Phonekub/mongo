# Mr.Supawit Hirunchai
# ID:6530300538
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://mongo:mongo@cluster0.cgejftk.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client["students"]
    collection = db["std_info"]
    while True:
        print("===MENU===")
        print("1: show all records")
        print("2: insert record")
        print("3: update record")
        print("4: delete record")
        print("5: exit")
        choice = input("Please choose:")
        choice = int(choice)
        if choice==1:
            print(f'found {collection.count_documents({})} records')
            all_students = collection.find()
            for std in all_students:
                print(std)
        elif choice==2:
            id=input("Input student id:")
            name=input("Input fullname:")
            major=input("Input major:")
            gpa=input("Input gpa:")
            gpa=float(gpa)
            try:
                collection.insert_one({"_id":id,
                                    "fullname":name,
                                    "major":major,
                                    "gpa":gpa
                                    })
                print("Success!")
            except Exception as e:
                print(e)
        elif choice==3:
            id=input("Input student id update:")
            name=input("Input fullname:")
            major=input("Input major:")
            gpa=input("Input gpa:")
            gpa=float(gpa)
            try:
                collection.update_many({"_id":id},
                                        {"$set":{"fullname":name,
                                                "major":major,
                                                "gpa":gpa}
                                        })
                print("Success!")
            except Exception as e:
                print(e)

        elif choice==4:
            id=input("Input student id to delete:")
            try:
                collection.delete_one({"_id":id})
                print("Success!")
                                        
            except Exception as e:
                print(e)
        
        elif choice==5:
            break
    
except Exception as e:
    print(e)
finally:
    client.close()