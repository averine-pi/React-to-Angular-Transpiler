#transpiler code
import re
#extract the component name
def extract_component(content):
    comp_name = re.search(r'function\s+(\w+)', content)
    if comp_name:
        return comp_name.group(1)
    
    comp_name = re.search(r'const\s+(\w+)\s*=', content)
    if comp_name:
        return comp_name.group(1)
    return "ConvertedComponent"
    
#extract the return portion for html
def extract_html(c):
    html_portion = re.search(r"return\s*\(([\s\S]*?)\);",c)
    return html_portion.group(1)

#main code to read the file
def generate_ts(file_path):
    with open(file_path, "r") as f:
        jsx_code = f.read()
        i = extract_component(jsx_code)
        comp_code = """@Component({selector:'app-todo-list',
        templateUrl:'./TodoList.component.html',
        styleUrls: ['./TodoList.component.css']})
        export class """ + f"""{i}"""+"Component"
        imp_stat = "import { Component } from '@angular/core';\n"
        # this writes the initial part of the program
        with open("angular_reference/demo.component.ts","w") as ts_file:
            ts_file.write(imp_stat)
            ts_file.write(comp_code)
            ts_file.write("{")
            ts_file.write("\n }")
            #actual code that has to run

def gen_template(file_path):
    with open(file_path,"r") as react_file:
        #read the contents of react file
        content = react_file.read()
        jsx_raw = get_jsxcode(content)
        #now time for replacing stuff
        #applying transformations
        new_code = apply_transformation(jsx_raw)
        with open("angular_reference/demo.component.html","w") as temp_file:
            temp_file.write(new_code)
        

def apply_transformation(jsx):
    modf = jsx
    modf = re.sub(r'onClick=\{(\w+)\}', r'(click)="\1()"', modf)
    modf = re.sub(r'onChange=\{[^}]*\}',"",modf)
    modf = re.sub(r'\{(\w+)\}', r'{{ \1 }}', modf)
    modf = re.sub(
    r'\{(\w+)\.map\(\((\w+),\s*(\w+)\)\s*=>\s*\(',
    r'<li *ngFor="let \2 of \1">',
    modf
    )
    
    modf = modf.replace("key={{ index }}", "")
    modf = re.sub(r'value=\{\{?\s*(\w+)\s*\}?\}', r'[(ngModel)]="\1"', modf)
    modf = modf.replace('))}', '') 
    modf = modf.replace(">)", ">").replace(") <", "<")
    return modf

def get_jsxcode(c):
    match = re.search(r"return\s*\(([\s\S]*)\)", c)
    if match:
        return match.group(1).strip()


react_file = r"C:\Users\Dell\OneDrive\Desktop\React_to_Angular_Transpiler_Task\react\TodoList.jsx"

generate_ts(react_file)
gen_template(react_file)
print("files generated...") 


        

