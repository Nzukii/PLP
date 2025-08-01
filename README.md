<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Innocent Mwendwa</title>
    <style>
        /* Cosmic Theme */
        :root {
            --space: #0a0e17;
            --star: #f5f9ff;
            --planet: #6d44b8;
            --comet: #4fc1e9;
            --alien: #a0d468;
            --text: #e6e9ee;
        }
        
        body, html {
    margin: 0;
    padding: 0;
}

        body {
            font-family: 'Courier New', monospace;
            background-color: var(--space);
            color: var(--text);
            margin: 0;
            padding: 0;
            background-image: 
                radial-gradient(circle at 10% 20%, var(--planet) 0%, transparent 20%),
                radial-gradient(circle at 90% 30%, var(--comet) 0%, transparent 25%),
                linear-gradient(to bottom, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.5) 100%);
            background-attachment: fixed;
            line-height: 1.6;
        }
        
        /* Starry background */
        body::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(1px 1px at 10% 20%, var(--star) 1px, transparent 2px),
                radial-gradient(1px 1px at 90% 30%, var(--star) 1px, transparent 2px),
                radial-gradient(1px 1px at 50% 80%, var(--star) 1px, transparent 2px),
                radial-gradient(1px 1px at 15% 50%, var(--star) 1px, transparent 2px),
                radial-gradient(1px 1px at 85% 70%, var(--star) 1px, transparent 2px);
            background-size: 100px 100px;
            z-index: -1;
        }
        
        header {
            text-align: center;
            padding: 0 1rem;
            position: relative;
        }
        
        h1 {
            font-size: 3rem;
            margin: 0;
            background: linear-gradient(to right, var(--comet), var(--alien));
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-shadow: 0 0 10px rgba(79, 193, 233, 0.3);
        }
        
        .tagline {
            font-style: italic;
            color: var(--comet);
            margin-top: 0.5rem;
        }
        
        .astronaut {
            font-size: 2rem;
            display: inline-block;
            animation: float 3s ease-in-out infinite;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-15px); }
        }
        
        nav {
            background-color: rgba(10, 14, 23, 0.8);
            backdrop-filter: blur(5px);
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
            padding: 1rem;
            margin: 0;
            flex-wrap: wrap;
        }
        
        nav li {
            margin: 0 1rem;
        }
        
        nav a {
            color: var(--text);
            text-decoration: none;
            font-weight: bold;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            transition: all 0.3s ease;
            position: relative;
        }
        
        nav a:hover {
            color: var(--alien);
            background-color: rgba(160, 212, 104, 0.2);
        }
        
        nav a::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            width: 0;
            height: 2px;
            background: var(--alien);
            transition: all 0.3s ease;
        }
        
        nav a:hover::after {
            width: 100%;
            left: 0;
        }
        
        section {
            padding: 2rem;
            max-width: 800px;
            margin: 0 auto;
            background-color: rgba(10, 14, 23, 0.7);
            border-radius: 15px;
            margin-bottom: 2rem;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(79, 193, 233, 0.1);
        }
        
        h2 {
            color: var(--alien);
            border-bottom: 2px solid var(--planet);
            padding-bottom: 0.5rem;
            display: inline-block;
            margin-top: 0;
        }
        
        .skills-container {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            margin-top: 1rem;
        }
        
        .skill {
            background-color: var(--planet);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.9rem;
            box-shadow: 0 3px 6px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease;
        }
        
        .skill:hover {
            transform: translateY(-5px);
            background-color: var(--comet);
        }
        
        .education-item {
            margin-bottom: 1.5rem;
            position: relative;
            padding-left: 1.5rem;
        }
        
        .education-item::before {
            content: '🛸';
            position: absolute;
            left: 0;
        }
        
        .education-item h3 {
            margin-bottom: 0.3rem;
            color: var(--comet);
        }
        
        .education-item p {
            margin-top: 0;
            color: var(--text);
        }
        
        form {
            display: grid;
            gap: 1rem;
        }
        
        input, textarea {
            background-color: rgba(255, 255, 255, 0.1);
            border: 1px solid var(--planet);
            border-radius: 5px;
            padding: 0.8rem;
            color: var(--text);
            font-family: inherit;
            width: 100%;
            box-sizing: border-box;
        }
        
        input:focus, textarea:focus {
            outline: none;
            border-color: var(--alien);
            box-shadow: 0 0 0 2px rgba(160, 212, 104, 0.3);
        }
        
        button {
            background-color: var(--alien);
            color: var(--space);
            border: none;
            padding: 1rem;
            border-radius: 5px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        button:hover {
            background-color: var(--comet);
            transform: translateY(-2px);
            box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
        }
        
        footer {
            text-align: center;
            padding: 2rem;
            color: var(--comet);
            font-size: 0.9rem;
        }
        
        .alien-emoji {
            font-size: 1.5rem;
            animation: blink 5s infinite;
        }
        
        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        
        @media (max-width: 600px) {
            h1 {
                font-size: 2rem;
            }
            
            nav ul {
                flex-direction: column;
                align-items: center;
            }
            
            nav li {
                margin: 0.5rem 0;
            }
            
            section {
                padding: 1rem;
            }
        }

        .profile-pic {
            display: block;
            margin: 1rem auto 0 auto;
            max-width: 150px;
            border-radius: 50%;
            box-shadow: 0 4px 16px rgba(0,0,0,0.3);
        }
    </style>
</head>
<body>
    <header>
        <div class="aspiring-developer">👩‍💻</div>
        <h1>Innocent Mwendwa</h1>
        <p class="tagline">Exploring the digital universe one line of code at a time. It is not easy!! (send help)</p>
        <img src="https://images.pexels.com/photos/26125152/pexels-photo-26125152.jpeg" alt="Innocent Mwendwa" class="profile-pic">
    </header>

    <nav>
        <ul>
            <li><a href="#about">About Me</a></li>
            <li><a href="#skills">Skills</a></li>
            <li><a href="#education">Education</a></li>
            <li><a href="#interests">Interests</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <main>
        <section id="about">
            <h2>📡 About Me</h2>
            <p>Greetings of peace! I'm Innocent, a beginner in software development. When I'm not freaking out about why a code I wrote is not running, I'm on Tiktok! lol!</p>
            <p>I'm especially passionate about blending technology and creativity to tell stories and connect people across the digital universe.</p>
        </section>
        
        <section id="skills">
            <h2>🚀 Programming Languages</h2>
            <p>My tech toolbox is always expanding, but here are the languages I'm currently learning but not super fluent in:</p>
            
            <div class="skills-container">
                <div class="skill">JavaScript</div>
                <div class="skill">Python</div>
                <div class="skill">HTML/CSS</div>
                <div class="skill">SQL</div>
            </div>
        </section>

        <section id="tech-stack">
    <h2>🧑‍🚀 Tech Stack</h2>
    <div style="display: flex; gap: 1.5rem; align-items: center; flex-wrap: wrap;">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" alt="HTML5" title="HTML5" width="40" height="40"/>
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" alt="CSS3" title="CSS3" width="40" height="40"/>
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" alt="JavaScript" title="JavaScript" width="40" height="40"/>
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" title="Python" width="40" height="40"/>
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" alt="MySQL" title="MySQL" width="40" height="40"/>
    </div>
</section>
        
        <section id="education">
            <h2>🎓 Educational Background</h2>
            
            <div class="education-item">
                <h3>Bachelor of ARTS </h3>
                <p>University of Nairobi| 2022-2026</p>
                <p>Specialized in Linguistics and History</p>
            </div>

            <div class="education-item">
            <h3>Certificate in Software Engineering and Development</h3>
            <p>ALX Africa | 2025</p>
            <p>Currently enrolled in a software development program to enhance my coding skills and build real-world applications.</p>
            </div>
            
            <div class="education-item">
                <h3>Certificate course in Computer Packages</h3>
                <p>Machakos Institute of Technology | 2022-2023</p>
                <p>Learned the basics of computer operations and software applications</p>
            </div>

            <div class="education-item">
                <h3>KENYA CERTIFICATE OF SECONDARY EDUCATION</h3>
                <p>Kaumoni Boys High School | 2018-2021</p>
                <p>Completed secondary education.</p>
            </div>

        </section> 
        <section id="interests">
            <h2>💡 Interests</h2>
            <p>When I'm not stressing about coding, I'm usually:</p>
            <ul>
                <li>Connecting with nature</li>
                <li>Teaching robots to understand human emotions (just kidding... or am I?)</li>
                <li>Exploring the latest tech trends</li>  
                <li>Worrying about due assignments</li>
                <li> Watching movies and sleeeping in</li>
            </ul>
            
            <p>I'm particularly excited about the intersection of technology and creativity, and how we can use code to tell stories and connect people across the digital universe.</p>
        </section>

        <section id="blog">
    <h2>📝 Blog & Articles</h2>
    <article>
        <h3>How I Survived My First Coding Project</h3>
        <p>Sharing my journey from confusion to clarity as I built my first website.</p>
    </article>
    <article>
        <h3>Why Learning to Code is Like Learning a New Language</h3>
        <p>Exploring the similarities between linguistics and programming. <a href="#">Read more...</a></p>
    </article>
    </section>

    <section id="fun-facts">
         <h2>🌟 Hobbies & Fun Facts</h2>
        <ul>
             <li>I can recite the alphabet backwards (try me!)</li>
             <li>Big fan of sci-fi movies and novels</li>
             <li>I love hiking and exploring new places</li>
             <li>My favorite programming snack: popcorn </li>
             <li>Fun fact: I once fixed a bug by taking a nap!</li>
    </ul>

        
        <section id="contact">
            <h2>📬 Contact Me</h2>
            <p>Want to collaborate on an out-of-this-world project? Have questions about my work or just about language andd History? Just want to say hello?</p>
            <p> Write me a message using this form or connect with me on the interwebs!</p>
            
            <form>
                <input type="text" placeholder="Your Name" required>
                <input type="tel" placeholder="Your Contact Number" required>    
                <input type="email" placeholder="Your Email" required>
                <textarea rows="5" placeholder="Your Message" required></textarea>
                <button type="submit">Beam Message</button>
            </form>
            <div class="contact-links">
                <h3>Connect with me:</h3>
                <a href="mailto:nzukiinnocent23@gmail.com" target="_blank">Email</a> |
                <a href="https://github.com/Nzukii/PLP" target="_blank">GitHub</a> |
                <a href="https://x.com/nz_uki?t=ZbBNtxD4qE71RACCNpFLAw&s=09" target="_blank">Twitter</a> |
                <a href="https://www.linkedin.com/in/innocent-mwendwa-53879a351?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank">LinkedIn</a>
            </div>
        </section>
    </main>
    
    <footer>
        <p>Made with <span class="alien-emoji">👽</span> and <span class="alien-emoji">💻</span> somewhere in the digital cosmos</p>
        <p>&copy; 2025 Innocent Nzuki . All rights reserved.</p>
    </footer>
</body>
</html>
