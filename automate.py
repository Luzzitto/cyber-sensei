videos = [
  {
    "title": "Introduction to Cybersecurity and Cyber Hygiene",
    "link": "https://www.youtube.com/watch?v=WbqMT3qfvJ8",
    "channel": "Cisco"
  },
  {
    "title": "The Importance of Cyber Hygiene",
    "link": "https://www.youtube.com/watch?v=nw_0vHJW8jk",
    "channel": "SecureLink"
  },
  {
    "title": "Cyber Hygiene and Security Best Practices",
    "link": "https://www.youtube.com/watch?v=bZMjHuaB92g",
    "channel": "RSA Conference"
  },
  {
    "title": "Cybersecurity: 5 Essential Practices for Protecting Yourself Online",
    "link": "https://www.youtube.com/watch?v=Ic1L2Cykikw",
    "channel": "The Daily Conversation"
  },
  {
    "title": "The Basics of Cyber Hygiene",
    "link": "https://www.youtube.com/watch?v=QT39qYzPWJ8",
    "channel": "Cybersecurity and Infrastructure Security Agency (CISA)"
  },
  {
    "title": "Cybersecurity for Everyone: Securing Your Home Network",
    "link": "https://www.youtube.com/watch?v=nNn6L5nHXf0",
    "channel": "NortonLifeLock"
  },
  {
    "title": "The Cybersecurity Experience: Cyber Hygiene",
    "link": "https://www.youtube.com/watch?v=fxNdQwmtMng",
    "channel": "University of Maryland Global Campus"
  },
  {
    "title": "The Importance of Cybersecurity Hygiene",
    "link": "https://www.youtube.com/watch?v=7lA6wnguV7k",
    "channel": "Deloitte"
  },
  {
    "title": "Protecting Your Business: Basic Cyber Hygiene",
    "link": "https://www.youtube.com/watch?v=3q48ZkP0ENI",
    "channel": "National Cyber Security Alliance"
  },
  {
    "title": "Cybersecurity and Cyber Hygiene Best Practices",
    "link": "https://www.youtube.com/watch?v=IOptR_K9cQs",
    "channel": "CyberScout"
  }
]


for v in videos:
    print(f"""
    <li class="cursor-pointer list-group-item border" link="{v["link"]}">
        <p>{v["title"]}</p>
        <small class="text-gray-400">{v["channel"]}</small>
    </li>
    """)