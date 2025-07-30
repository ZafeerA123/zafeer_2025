import requests
import json

WEBHOOK = "https://hook.us2.make.com/qlnuuhstm25oxmlft55qgyhlfd7m5t45"
RAPIDAPI_KEY = "2d7756c4fdmshd83860277df937ep15bfe9jsnc4301a012ef9"  # your key

def fetch_trending():
    url = "https://tiktok-api23.p.rapidapi.com/api/post/trending?count=10"
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "tiktok-api23.p.rapidapi.com"
    }

    res = requests.get(url, headers=headers)
    data = res.json().get("itemList", [])

    trends = []
    for item in data:
        try:
            video_id = item["id"]
            user = item["author"]["uniqueId"]
            caption = item.get("desc", "No caption")
            likes = item.get("stats", {}).get("diggCount", 0)
            trends.append({
                "text": caption,
                "diggCount": likes,
                "webVideoUrl": f"https://www.tiktok.com/@{user}/video/{video_id}"
            })           
        except Exception as e:
            print("Skipping item due to error:", e)

    return trends

def send_to_make(data):
    payload = {"trends": data}
    headers = {"Content-Type": "application/json"}
    res = requests.post(WEBHOOK, json=payload, headers=headers)
    print("Sent to Make.com. Status:", res.status_code)
    print(json.dumps(payload, indent=2))

if __name__ == "__main__":
    videos = fetch_trending()
    if videos:
        send_to_make(videos)
    else:
        print("No videos found.")
