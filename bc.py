import requests
from rich.console import Console
from tqdm import tqdm
import sys

# initialize console for rich output
console = Console()

# set constant values for the process
url = "https://hackerone.com/graphql"
reporter = sys.argv[1]

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
    "content-type": "application/json",
    "cookie": "h1_device_id=a628af4d-5408-4319-9188-b8c3c4fcc450; intercom-id-zlmaz2pu=955779aa-7ca2-40f0-99a8-c0ac36bf247b; intercom-device-id-zlmaz2pu=c8125926-2c3c-4fcb-a49b-d638a497937f; cf_clearance=0iqtT7ph35gvkPkj98TQk2R3jzllIxfOMDnj9ECQmt4-1727710216-1.2.1.1-Edtp71ZI2TRqJOAlOLpb.6AnAYAXsJyZkhb7Q174evwNGWURbjPvLsJvIxF8bpAsTZsrhOCI9HllpCkEAldylxzMyfLKdPAZS44MTsvEmJpRVAYq9nWcG5N5eP0UaNK1XxptqRqAgLC9CFFv4ig0xIE0f.auCqP1L5u7FflzmFe3YdMR7wCRDEPCN8XPbFj7DfgqaeDcfgvdP9ly6PwtCtW9UcTMHyY0arFUVw4oFEB0eKUPcArYKKHbc_s_v8FhxH5rclSVgWz2dCw7B0kbjGYKb07arTGfTbeXaMHtX9KVTvETxZ8sErOFYDOOHKv_p69EUhO.am5yarrpsc7M5kLohnTUfwdJhzJYNs06QP1nD6pqiWHQ1U7bKu0_0MaDvPpMgpQMxmrgInIF6X8yqfVWrpd_lLRmkqtw5CVOs7w; notice_preferences=0:; TAconsentID=1adc1585-01d6-45d4-8b6e-38650a15c401; notice_gdpr_prefs=0:; cmapi_gtm_bl=ga-ms-ua-ta-asp-bzi-sp-awct-cts-csm-img-flc-fls-mpm-mpr-m6d-tc-tdc; cmapi_cookie_privacy=permit 1 required; optimizelyEndUserId=oeu1728737615989r0.99752818350901; intercom-session-zlmaz2pu=bzA1UWZVdyt0Z2w1czRRQVdRRUc4U1pCdVJTNkNBajN2U1Y5ZWN2M3RGdUJVL3I4QUpjTEswK1lCYUdhRE93Vi0tYld6bVdra1k4NTlNcVpxaVg2b3hnZz09--8c50ce07e014278ad037af60d07ff8d1b3a2ba63; _cfuvid=8JRxQLlD228lyDkQE7OblFvYFOne0YPFs0tPaFiLIi8-1728960946193-0.0.1.1-604800000; notice_behavior=implied,eu; __Host-session=VVZxaW1Ha2hHZVRvZlZ6TytSTmhWVFBIRGg3SWlDcTVWc2E1UnQ4ZjlBSllEYno1MUFNcXYzdjdSZWFvYmZVejJOdkJiU3hTaFo5UDlSSzF4cmU0YmJjdTlxZlpjTTE4T25QQ1NPMmJVKzdYdm5QNEZjYXlsWE9rMm40Y0VLdUd2REZYeGFsak1wRTR6V1JkSjRBenAveG5Hc0syNi94Wnhoc2FTUVB0aU1jVjR5S0pwNXJSbkMzRjdVbW1RUUw1b2pGbCtEY0hMdUozeDZlMnd2UXhMZjNOMnkzcGNPUVdQNDNCVlJnZWdvUmVaQXVuaXN6R1owS0F3RDVZRmlVd2REVE1lM09EWGxEbVJzeFBNQ1hWTmxKQmJiQXNFM2RGMnZMZlphZXBQWmtxMkJiaStOU0c1dVRVYTBQTzAvRTZXRkFOaHdzQnpNMWgzdk9QVmFNMFpIUDQ0aWlMa1NrOExpRzloT2ZwU0g3TjJ6N0FoWkdhMnl0Mk9wRG5Kckk0WFJ3Rng2NktJWEczeGR2RkxlUTZ4UT09LS1adGpGR0FScHczMzIxcVYwRnk4QjJ3PT0=--8c3fd3e0d050e262e8a630767309a616ee6bc7b0",
    "dnt": "1",
    "origin": "https://hackerone.com",
    "priority": "u=1, i",
    "referer": f"https://hackerone.com/{reporter}/hacktivity?type=user", # simulate a real browser action by applying a referer header
    "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"129.0.6668.101\"",
    "sec-ch-ua-full-version-list": "\"Google Chrome\";v=\"129.0.6668.100\", \"Not=A?Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"129.0.6668.100\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"15.0.0\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "x-csrf-token": "glC6d1isdZe34wXAw0U4Zit8OOxBEJ9Uk3jYhHPURyDPP+fW830uQYgV39WIgczeQ0578j7Bh6r0wsT5m2bVPw==", # we're unautheticated anyways, the csrf token doesn't matter
    "x-product-area": "hacktivity",
    "x-product-feature": "overview"
}

def fetch_nodes():
    console.rule("[bold red]Fetching Hacktivity Reports...[/bold red]")
    
    batch_size = 1000
    from_offset = 0
    nodes = []
    
    while True:
        # adjust the 'from' value dynamically for pagination - simulate the hackerone pagination
        data = {
            "operationName": "HacktivitySearchQuery",
            "variables": {
                "queryString": f'reporter:("{reporter}")',
                "size": batch_size,
                "from": from_offset,
                "sort": {
                    "field": "latest_disclosable_activity_at",
                    "direction": "DESC"
                },
                "product_area": "hacktivity",
                "product_feature": "overview"
            },
            "query": """
            query HacktivitySearchQuery($queryString: String!, $from: Int, $size: Int, $sort: SortInput!) {
            me {
                id
                __typename
            }
            search(
                index: CompleteHacktivityReportIndex
                query_string: $queryString
                from: $from
                size: $size
                sort: $sort
            ) {
                __typename
                total_count
                nodes {
                __typename
                ... on HacktivityDocument {
                    id
                    _id
                    reporter {
                    id
                    username
                    name
                    __typename
                    }
                    cve_ids
                    cwe
                    severity_rating
                    upvoted: upvoted_by_current_user
                    public
                    report {
                    id
                    databaseId: _id
                    title
                    substate
                    url
                    disclosed_at
                    report_generated_content {
                        id
                        hacktivity_summary
                        __typename
                    }
                    __typename
                    }
                    votes
                    team {
                    id
                    handle
                    name
                    medium_profile_picture: profile_picture(size: medium)
                    url
                    currency
                    __typename
                    }
                    total_awarded_amount
                    disclosed
                    has_collaboration
                    __typename
                }
                }
            }
            }
            """
        }

        # send the POST request to hackerone API
        response = requests.post(url, headers=headers, json=data)
        response_nodes = response.json()["data"]["search"]["nodes"]

        if response.status_code != 200:
            console.print(f"[bold red]Error: Failed to fetch reports! Status Code: {response.status_code}[/bold red]")
            break

        # if the nodes are empty in the response, then there's no more reports left
        if not response_nodes:
            break

        # add to the nodes array
        nodes = nodes + response_nodes
        
        # increment the offset for pagination
        from_offset += batch_size
    
    return nodes

def main():
    # fetch and process nodes with live counter
    nodes = fetch_nodes()
    total_rewards = 0

    # Display live progress with tqdm
    for node in tqdm(nodes, desc="Processing reports", unit="report"):
        total_awarded_amount = node.get("total_awarded_amount", 0) # set to 0 if none
        if total_awarded_amount is not None:
            total_rewards += int(total_awarded_amount)
        
        # Update live counter
        console.print(f"[cyan] Current Total Rewards: [bold green]{total_rewards} USD[/bold green]", end='\r')
    
    # Display final total rewards
    console.print(f"\n[bold green]User [bold yellow]{reporter}[/bold yellow] has made over [yellow]{total_rewards}.00 USD[/yellow] in total rewards![/bold green]")
    console.print(f"[yellow]Keep in mind that doesn't include any private programs nor undisclosed bounties[/yellow]")
    console.print(f"[yellow]That's just the public reports with the show bounty option enabled[/yellow]")

if __name__ == "__main__":
    main()
