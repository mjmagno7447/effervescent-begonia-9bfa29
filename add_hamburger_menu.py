import os
import glob

html_files = glob.glob("*.html")

# Hamburger icon button to add after brand
hamburger_button = '''<button class="hamburger-menu" id="hamburgerBtn" aria-label="Toggle navigation">
        <span></span>
        <span></span>
        <span></span>
      </button>'''

# Hamburger CSS to add to styles.css
hamburger_css = '''.hamburger-menu{display:none;flex-direction:column;background:none;border:none;cursor:pointer;padding:0;width:30px;height:30px;gap:6px}.hamburger-menu span{width:30px;height:3px;background:#fff;transition:all 0.3s ease;display:block}.hamburger-menu.active span:nth-child(1){transform:rotate(45deg) translate(8px,8px)}.hamburger-menu.active span:nth-child(2){opacity:0}.hamburger-menu.active span:nth-child(3){transform:rotate(-45deg) translate(7px,-7px)}@media (max-width:980px){.hamburger-menu{display:flex}.nav-links{position:fixed;top:60px;left:0;right:0;background:rgba(0,0,0,0.95);flex-direction:column;gap:0;padding:20px;max-height:0;overflow:hidden;transition:max-height 0.3s ease}.nav-links.active{max-height:300px}.nav-links a{padding:15px 0;border-bottom:1px solid rgba(255,255,255,0.1)}.nav-links a:last-child{border-bottom:none}}'''

# Hamburger JavaScript
hamburger_js = '''<script>const hamburgerBtn = document.getElementById('hamburgerBtn');const navLinks = document.querySelector('.nav-links');if(hamburgerBtn){hamburgerBtn.addEventListener('click',()=>{hamburgerBtn.classList.toggle('active');navLinks.classList.toggle('active');});document.querySelectorAll('.nav-links a').forEach(link=>{link.addEventListener('click',()=>{hamburgerBtn.classList.remove('active');navLinks.classList.remove('active');});});};</script>'''

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if hamburger already added
    if 'hamburger-menu' in content:
        print(f"Skipped {html_file} - hamburger menu already exists")
        continue
    
    # Add hamburger button after brand
    if 'class="brand"' in content and 'class="nav-links"' in content:
        # Find closing div after brand
        brand_pos = content.find('class="brand"')
        brand_close = content.find('</div>', brand_pos)
        insert_pos = brand_close + 6
        content = content[:insert_pos] + '\n      ' + hamburger_button + content[insert_pos:]
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added hamburger menu to: {html_file}")
    else:
        print(f"Could not find nav structure in {html_file}")

# Add hamburger CSS to styles.css
with open('css/styles.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

if '.hamburger-menu' not in css_content:
    css_content = css_content + hamburger_css
    with open('css/styles.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("Added hamburger CSS to styles.css")
else:
    print("Hamburger CSS already exists in styles.css")

print("Hamburger menu setup complete!")
print("\nNote: Add this JavaScript before </body> tag in each HTML file:")
print(hamburger_js)
