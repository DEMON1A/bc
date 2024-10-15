# bc
Bounty calculator for HackerOne users that have the display rewards option enabled

## How to install and use
```bash
git clone https://github.com/DEMON1A/bc
cd bc
pip install rich tqdm
python bc.py todayisnew
```

## How it works
Bounty calculator is using HackerOne hacktivity API in order to retrive every single report made by that user as nodes, looping over every single node it calculates the total rewards this user has been awarded

**Keep in mind that doesn't include any private programs nor undisclosed bounties,
That's just the public reports with the show bounty option enabled**
