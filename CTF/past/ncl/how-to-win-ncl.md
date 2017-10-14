
source: wraysec.com/2015/11/02/how-to-win-the-ncl/

The National Cyber League, also known as the NCL, is a collegiate cyber security program. It’s more than just a competition, but a full season-long training platform. NCL was created to provide an ongoing virtual training ground for collegiate students to develop, practice, and validate their cyber security skills using next-generation, high-fidelity simulation environments. The league provides a means for the participants to prepare and test themselves against today’s security challenges.

Participants in the NCL aren’t just playing in a competitive game, they are also given access to practical and real-world training labs to learn and hone their craft. Furthermore, the program has had much success linking directly into the classroom, through the parent organization, The National CyberWatch Center. The NCL provides standardized curriculum in assisting schools towards delivering cutting-edge programs to prepare their students.

The combination that the NCL provides is like no other, but it all culminates in a puzzle-based, capture-the-flag style, cyber competition. The competition is broken down into three distinct parts: The Preseason, The Regular Season, and The Post-season. The Preseason and Regular Season are both individual-based; however, the Post-Season is team based, made up of players from each individual university or college.

During the Preseason, participants are assessed and placed into one of three brackets based on their current skill set: Bronze, Silver, or Gold.

So, how do you win the NCL? Read the following tips, and don’t worry, we’ll cover some technical ones too!
Prepare:

No matter if you’re a Gold player or a Bronze player, don’t overlook the NCL labs. While you may feel you already have sufficient skills in areas the labs are covering, the puzzles and challenges are going to be based on those labs. Many times small hints or tricks will be discussed in the lab, then implemented in a puzzle during the competition.

The NCL provided materials aren’t the only place you can look. NCL has been around since May of 2011, and there have been many participants before you. It’s extremely common for players, especially those who have won, to discuss their tactics after the fact. Take a look around online and you’ll find write-ups for old puzzles and lessons along the way. Seriously, don’t overlook this valuable data, it might just give you the edge you need.
Keep It Simple:

There is no question, cyber exercises are designed to test your critical thinking skills. They very often force you to think outside of the box. That doesn’t mean the answer has to be complex. Start with the basics. Over-thinking a problem is one of the most common pitfalls a player faces, and they end up spending valuable time and resources over-engineering. Time is something you can’t make up in a competition.
Easy Or Hard, Where To Start:

This is a question every player will face. The play clock starts and the competition is on! Now, what do you go after first? The low hanging fruit or the big points? It’s not something we can answer in a blog post, it’s just too subjective and personal, but here are some tips.

Use your time wisely. Some puzzles require time. If you have a slew of password hashes to crack, don’t wait until the last minute to fire up John The Ripper, get started right away. You don’t have to be the first to submit the answers, but when ready you’ll have them waiting for you, instead of running out of time.

Play to your strengths. If you’re really good at Web Exploitation, it makes sense to start there, regardless of whether you’re going for the easy puzzles or the hard ones. Get the stuff you’re comfortable with out of the way.

Bounce around and know when to move on. Don’t get stuck, keep moving. Nobody is forcing you to complete the challenges in any particular order. If you come across a puzzle that you just can’t solve, sometimes moving on is your best bet. Don’t forget about the problem or give up, but move on to another challenge in the meantime. This not only ensures you’re still getting points on the board, but you will generate some mental clarity by taking a break.
Know Linux and Use It:

It doesn’t matter if you’re a Windows guys or a Mac girl, the fact of the matter is Linux was built for this. You can use whatever OS you want, but have a Linux VM around. The command-line tools offered in Linux can make some of the challenges a breeze. And many security tools only offer a Linux version.

We recommend having a copy of Kali – https://www.kali.org/. If you’re unfamiliar with Kali it’s a Linux distribution with most of the commonly used security tools pre-installed. Better yet, there are tons of resources to help you learn how to use Kali if you’re newer to the distribution.

Another recommendation, even for veteran Linux users is a cheat-sheet. There are a lot of Linux utilities. Check out a few of the following guides, and keep them handy during the competition events:

    http://files.fosswire.com/2007/08/fwunixref.pdf
    http://www.digilife.be/quickreferences/QRC/The%20One%20Page%20Linux%20Manual.pdf
    http://cb.vu/unixtoolbox.xhtml

Know Your Tools:

Half of the difference between a skilled security professional and a novice is knowing what tool to use for the job, and well, know what the tool does. There was a time when script kiddie was used to describe someone who didn’t write their own tools, but those days are gone. When was the last time your wrote your own text editor, built your own display drivers, or compiled a kernel from source? (Okay, the last one might still be common with some in the crowd, but by-in-large it too is rare today).

Today script kiddie is more about the definition of knowing your tools, how they operate, and what they do under the hood. This is very important both in cyber exercises and the real world. Things break. Stuff goes wrong. It’s important you know how to get back on track. If you’re simply pulling the trigger, it’s really hard to readjust if things don’t just fall in line. So make sure you take time to learn the tools you plan to use during the competition.
Web Application Exploitation:

Web Applications are all the rage nowadays, especially in the security field, and why wouldn’t they be? The World Wide Web we have today might not be what Tim Berners-Lee had envisioned, but it’s what we got. Everyone, everywhere is moving everything to the “web.” HTTP has become more of a transport layer than an application layer, so of course it’s huge in the security world.

So how do you tackle a web application in the NCL? Well, don’t forget the basics. Start with analyzing the functionality; What does the application do? How would a typical “user” interact with the site? Keep an eye out for functionality that could lead to exploitation.

If the web application accepts files for upload, it’s fairly likely you’ll find some sort of file upload vulnerability. If the application has a database back-end and utilizes user-input for functionality, it’s pretty likely you’ll find some SQL Injection vulnerability.

As you’re going through the application pay particular attention the source code you can see; the HTML, JS, and CSS being delivered to your browser. You could simply Right Click and select View Source, but we’d recommend a better method. Use one of the many different Web Development plugins for your browser. Firefox has the much revered Firebug, and Chrome has a fairly decent tool built in called Developer Tools.

These tools not only give you access to the live source code in your browser, they let you view and edit everything- from the code, to your cookies, to the style sheets. With these tools you can view the network requests that are taking place, and that will give you plenty of insight into how the application works behind the scenes.

Here are a few more Firefox plugins that you won’t want to compete without:

    Tamper Data
    Web Developer Toolbar
    XSS Me
    SQL Inject Me
    HackBar

Along the lines of the basics, don’t forget how web servers work either. Lots of information can be gleaned from things like the headers (viewable in the Net tabs of your Developer tool). Also think of the places an admin would utilize to restrict access: robots.txt, .htacces, .htpasswd, etc. These might just give you the answer, or at the very least point you in the right direction.

Next you’ll want to be on your A-Game with SQL Injection. Make sure you have tools like sqlmap down cold. This particular tool is fairly automated, but knowing the tips and tricks can really help. Here’s a cheat sheet you might find useful: https://github.com/aramosf/sqlmap-cheatsheet/blob/master/sqlmap%20cheatsheet%20v1.0-SBD.pdf

Make sure you have some command-line web tools ready to go. wget and curl are great for crafting web requests exactly as you’ll need them. This becomes especially useful when the browser’s security features are getting in the way of performing the action you’re trying. These tools also will allow you to do non-standard requests, which might just be necessary during the competition. Here’s a curl cheat sheet: http://www.cheatography.com/ankushagarwal11/cheat-sheets/curl-cheat-sheet/ and here’s a wget cheat sheet: https://github.com/mcandre/cheatsheets/blob/master/wget.md.

We have one last suggestion for the Web Application Exploitation category: Don’t spam the web servers with automated tools. It’s not impossible, but rare that the answers are just going to fall out with a simple nikto run. And one thing is for certain, running nikto hundreds of times isn’t going to net you any different results.
Encryption and Encoding:

Encryption and Encoding challenges really go to the core of the puzzles. If you’ve ever found yourself passing time on a flight by solving anagrams, you’ll fare well in this category. If not, there are some very valuable resources to help make this process easier. Here are a few resources that are a must have during the competition:

    http://rumkin.com/tools/cipher/ (our favorite)
    http://quipqiup.com/
    http://aesencryption.net/
    http://www.asciitohex.com/
    https://www.tools4noobs.com/online_tools/encrypt/
    http://www.md5online.org/
    http://www.xorbin.com/tools

Traffic Analysis:

Network Traffic Analysis is a real-world challenge, and one that commonly finds its way into competitions. tcpdump is your friend. Sure, you could use Wireshark for some graphical fun, but the power of tcpdump is unrivalled. Combine tcpdump with a handful of other Linux command-line tools like grep, sed, and awk, and you have a powerhouse on your hands. Here’s a tcpdump cheat sheet: http://packetlife.net/media/library/12/tcpdump.pdf. Seriously, learn this tool and use it.

tcpdump isn’t the only tool useful when going through PCAP data. Check out these tools as well, as they will be invaluable during the NCL:

    tcpflow
    tcpick
    tshark
    tcpxtract
    NetworkMiner (Windows-Based)
    Foremost
    bro
    snort

Other Tools:

Here’s a list of a few more tools (mostly command-line) you’ll want to be familiar with before the events:

    cat / less / more
    strings
    hexdump
    xxd
    grep
    sed
    awk
    gdb (GNU Debugger)

We hope these tools and tips are useful during your NCL adventure. Good luck! And don’t forget to mention your NCL experience on your resume.

You can learn more about the NCL on their website: http://www.nationalcyberwatch.org/

You can learn more about the National CyberWatch Center on their website: http://www.nationalcyberwatch.org/
