import os
import glob

html_files = glob.glob("*.html")

hamburger_js = '''
  <script>const hamburgerBtn = document.getElementById('hamburgerBtn');const navLinks = document.querySelector('.nav-links');if(hamburgerBtn){hamburgerBtn.addEventListener('click',()=>{hamburgerBtn.classList.toggle('active');navLinks.classList.toggle('active');});document.querySelectorAll('.nav-links a').forEach(link=>{link.addEventListener('click',()=>{hamburgerBtn.classList.remove('active');navLinks.classList.remove('active');});});};</script>
'''

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if hamburger JS already added
    if 'hamburgerBtn' in content:
        print(f"Skipped {html_file} - hamburger JS already exists")
        continue
    
    # Add hamburger JS before </body>
    if '</body>' in content:
        content = content.replace('</body>', hamburger_js + '</body>')
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added hamburger JS to: {html_file}")
    else:
        print(f"Could not find </body> in {html_file}")

print("Hamburger menu JavaScript added to all HTML files!")
