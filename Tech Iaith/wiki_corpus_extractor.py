import requests
import json
import time


def get_page_content(api_url, pageid, session):
    params = {
        "action": "query",
        "prop": "revisions",
        "rvprop": "content",
        "rvslots": "main",
        "pageids": pageid,
        "format": "json",
    }

    response = session.get(api_url, params=params)
    if response.status_code != 200:
        print(f"Failed to get page content: {response.status_code}")
        return None

    data = response.json()
    pages = data.get("query", {}).get("pages", {})
    page = pages.get(str(pageid), {})
    revisions = page.get("revisions", [])

    if not revisions:
        return None

    content = revisions[0].get("slots", {}).get("main", {}).get("*", "")
    if "{{person" in content.replace("\n", "").lower():
        print(f"Found person template in {pageid}")
        fr = content[content.find("fr=") + 3 :]
        fr = fr[: fr.find("|")].strip()
        br = content[content.find("br=") + 3 :]
        br = br[: br.find("|")].strip()
        return {"br": br, "fr": fr}
    else:
        print("nothing found")
        pass


# Function to authenticate and get the CSRF token
def get_csrf_token(session, api_url, username, password):
    # Log in to get a session cookie
    session.headers.update({"User-Agent": "YourScript/1.0 (alan.kersaudy@email.com)"})
    login_token = session.get(
        api_url,
        params={"action": "query", "meta": "tokens", "type": "login", "format": "json"},
    )
    login_token = login_token.json()["query"]["tokens"]["logintoken"]
    session.post(
        api_url,
        data={
            "action": "login",
            "username": username,
            "password": password,
            "loginreturnurl": api_url,
            "logintoken": login_token,
            "format": "json",
        },
    )

    # Get CSRF token
    csrf_token = session.get(
        api_url, params={"action": "query", "meta": "tokens", "format": "json"}
    ).json()["query"]["tokens"]["csrftoken"]

    return csrf_token


def get_category_members(api_url, category, session):
    params = {
        "action": "query",
        "list": "categorymembers",
        "cmtitle": category,
        "cmlimit": "500",
        "format": "json",
    }

    response = session.get(api_url, params=params)
    if response.status_code != 200:
        print(f"Failed to get category members: {response.status_code}")
        return []

    data = response.json()
    members = data.get("query", {}).get("categorymembers", [])
    return [(page.get("title"), page.get("pageid")) for page in members]


# Function to upload content to Wikimedia
def download_sentences(api_url, username, password, category):
    session = requests.Session()

    csrf_token = get_csrf_token(session, api_url, username, password)
    print("csrf_token", csrf_token)

    response = session.get(
        api_url,
        data={
            "action": "get",
            "title": "Rummad:Korpus_fr-br",
            "token": csrf_token,
            "format": "json",
        },
    )
    print(f"Getting pages in {category}")
    pages = get_category_members(api_url, category, session)
    print(f"Found {len(pages)} pages")

    # Get content for each page
    all_example = []
    for i, (title, pageid) in enumerate(pages):
        print(f"Processing {i+1}/{len(pages)}: {title}")
        content = get_page_content(api_url, pageid, session)
        if content:
            all_example.append(content)
            print("downloaded:", content)
        else:
            print(f"No content found for {title}")

        # Be nice to the server
        time.sleep(1)

    # Save all content
    with open("corpus_content.json", "w", encoding="utf-8") as f:
        json.dump(all_example, f, ensure_ascii=False, indent=2)

    print(f"Saved content from {len(all_example)} pages to korpus_content.txt")


api_url = "https://style.miraheze.org/w/api.php"
username = "Alan Kersaudy"
password = ""
category = "Category:Korpus_fr-br"

# upload_page_to_wiki("Test", "This is a test page", api_url, username, password)

download_sentences(api_url, username, password, category)
