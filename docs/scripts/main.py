env.variables['term_counter'] = 0
env.variables['REPL_counter'] = 0

@env.macro
def terminal() -> str:
    """   
    Purpose : Create a Python Terminal.
    Methods : Two layers to avoid focusing on the Terminal. 1) Fake Terminal using CSS 2) A click hides the fake 
    terminal and triggers the actual Terminal.
    """        
    tc = env.variables['term_counter']
    env.variables['term_counter'] += 1
    return f"""<div onclick='start_term("id{tc}")' id="fake_id{tc}" class="terminal_f"><label class="terminal"><span>>>> </span></label></div><div id="id{tc}" class="hide"></div>"""

def read_ext_file(nom_script : str) -> str:
    """
    Purpose : Read a Python file that is uploaded on the server.
    Methods : The content of the file is hidden in the webpage. Replacing \n by a string makes it possible
    to integrate the content in mkdocs admonitions.
    """
    short_path = f"""docs/{os.path.dirname(env.variables.page.url.rstrip('/'))}"""
    try: 
        f = open(f"""{short_path}/scripts/{nom_script}.py""")
        content = ''.join(f.readlines())
        f.close()
        content = content+ "\n"
        # Hack to integrate code lines in admonitions in mkdocs
        return content.replace('\n','backslash_newline')
    except :
        return
    
def generate_content(nom_script : str) -> str:
    """
    Purpose : Return content and current number REPL {tc}.
    """
    tc = env.variables['REPL_counter']
    env.variables['REPL_counter'] += 1

    content = read_ext_file(nom_script)

    if content is not None :
        return content, tc
    else : return "", tc

def create_upload_button(tc : str) -> str:
    """
    Purpose : Create upoad button for a REPL number {tc}.
    Methods : Use an HTML input to upload a file from user. The user clicks on the button to fire a JS event
    that triggers the hidden input.
    """
    return f"""<button class="emoji" onclick="document.getElementById('input_editor_{tc}').click()">⤴️</button>\
            <input type="file" id="input_editor_{tc}" name="file" enctype="multipart/form-data" class="hide"/>"""

def create_unittest_button(tc : str, nom_script: str, mode) -> str:
    """
    Purpose : Generate the button for REPL {tc} to perform the unit tests if a valid test_script.py is present.
    Methods : Hide the content in a div that is called in the Javascript
    """
    stripped_nom_script = nom_script.split('/')[-1]
    relative_path = '/'.join(nom_script.split('/')[:-1])
    nom_script = f"{relative_path}/test_{stripped_nom_script}"
    content = read_ext_file(nom_script)
    if content is not None: 
        return f"""<span id="test_term_editor_{tc}" class="hide">{content}</span><button class="emoji_dark" onclick=\'executeTest("{tc}","{mode}")\'>🛂</button><span class="compteur">5/5</span>"""
    else: 
        return ''


def blank_space() -> str:
    """ 
    Purpose : Return 5em blank spaces. Use to spread the buttons evenly
    """
    return f"""<span style="indent-text:5em"> </span>"""

@env.macro
def REPLv(nom_script : str ='') -> str:
    """
    Purpose : Easy macro to generate vertical REPL in Markdown mkdocs.
    Methods : Fire the REPL function with 'v' mode.
    """
    return REPL(nom_script, 'v')


@env.macro
def REPL(nom_script : str ='', mode : str = 'h') -> str:
    """
    Purpose : Create a REPL (Editor+Terminal) on a Mkdocs document. {nom_script}.py is loaded on the editor if present. 
    Methods : Two modes are available : vertical or horizontal. Buttons are added through functioncal calls.
    Last span hides the code content of the REPL if loaded.
    """
    content, tc = generate_content(nom_script)
    corr_content, tc = generate_content("corr_"+nom_script)
    div_edit = f'<div class="repl_classe">'
    if mode == 'v':
        div_edit += f'<div class="wrapper"><div class="interior_wrapper"><div id="editor_{tc}"></div></div><div id="term_editor_{tc}" class="term_editor"></div></div>'
    else:
        div_edit += f'<div class="wrapper_h"><div class="line" id="editor_{tc}"></div><div id="term_editor_{tc}" class="term_editor_h terminal_f_h"></div></div>'
    div_edit += f"""<button class="emoji" onclick='interpretACE("editor_{tc}","{mode}")'>▶️</button>"""
    div_edit += f"""{blank_space()}<button class="emoji" onclick=\'download_file("editor_{tc}","{nom_script}")\'>⤵️</button>{blank_space()}"""
    div_edit += create_upload_button(tc)
    div_edit += create_connect_button_numworks(tc)
    div_edit += create_upload_button_numworks(tc)
    div_edit += create_unittest_button(tc, nom_script, mode)
    div_edit += '</div>'

    div_edit += f"""<span id="content_editor_{tc}" class="hide">{content}</span>"""
    div_edit += f"""<span id="corr_content_editor_{tc}" class="hide">{corr_content}</span>"""
    return div_edit