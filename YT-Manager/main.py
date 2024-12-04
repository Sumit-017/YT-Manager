from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://<user-name>:<password>@<db-name>.lkvno.mongodb.net/")
db = client["YoutubeManager"]
video_collection = db["videos"]
# print(video_collection)

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']} || Name : {video['name']} || Duration : {video['time']}")

def update_video(video_id, new_name, new_time):
    video_collection.update_one(
    {'_id' : ObjectId(video_id)},
    {"$set" : {"name": new_name, "time": new_time}}
    )
def delete_video(video_id):
    video_collection.delete_one({'_id' : ObjectId(video_id)})


def main():
    while True:
        print("Your Own || YT Manager App")
        print("1.list your all videos.")
        print("2.Add a new video.")
        print("3.Update a video.")
        print("4.Delete a video.")
        print("5.Exit the app.")
        choice = input("Enter your choice: ")
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the name of the video: ")
            time = input("Enter the duration of the video: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video id to update: ")
            name = input("Enter the name of the video to be updated: ")
            time = input("Enter the duration of the video to be updated: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter video ID to update: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice.")

if __name__ == "__main__":
    main()