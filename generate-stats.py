import json

with open("github-stats.json", "r") as f:
    data = json.load(f)

stats = data["data"]["user"]["contributionsCollection"]

items = [
    ("Commits", stats["totalCommitContributions"]),
    ("Issues", stats["totalIssueContributions"]),
    ("Pull Requests", stats["totalPullRequestContributions"]),
    ("PR Reviews", stats["totalPullRequestReviewContributions"]),
    ("Repositories", stats["totalRepositoryContributions"]),
]

max_value = max(value for _, value in items) or 1

width = 800
height = 420

svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{width}" height="{height}"
viewBox="0 0 {width} {height}">

<rect width="100%" height="100%" rx="20" fill="#0d1117"/>

<text x="40" y="55"
font-family="Arial"
font-size="28"
font-weight="bold"
fill="#ffffff">
GitHub Contributions
</text>
'''

y = 100

for name, value in items:
    bar_width = int((value / max_value) * 600)

    svg += f'''
<text x="40" y="{y}"
font-family="Arial"
font-size="17"
fill="#c9d1d9">
{name}
</text>

<rect x="170" y="{y-18}"
width="600" height="24"
rx="12"
fill="#21262d"/>

<rect x="170" y="{y-18}"
width="{bar_width}" height="24"
rx="12"
fill="#58a6ff"/>

<text x="785" y="{y}"
text-anchor="end"
font-family="Arial"
font-size="16"
fill="#ffffff">
{value}
</text>
'''
    y += 60

svg += "</svg>"

with open("github-stats.svg", "w") as f:
    f.write(svg)

print("GitHub stats chart generated!")
