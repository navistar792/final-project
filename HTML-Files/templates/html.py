from languages import languages
import pandas as pd

for x in languages:
    print(
        f'<input type="checkbox" name="checkbox"  value="{x}" /><label>{x}</label><br>'
    )



# (
# <input type="checkbox" name="checkbox"  value=AWS /><label>AWS</label><br>
# <input type="checkbox" name="checkbox"  value=Bash/Shell /><label>Bash/Shell</label><br>
# <input type="checkbox" name="checkbox"  value=C++ /><label>C++</label><br>
# <input type="checkbox" name="checkbox"  value=COBOL /><label>COBOL</label><br>
# <input type="checkbox" name="checkbox"  value=Cassandra /><label>Cassandra</label><br>
# <input type="checkbox" name="checkbox"  value=Clojure /><label>Clojure</label><br>
# <input type="checkbox" name="checkbox"  value=Crystal /><label>Crystal</label><br>
# <input type="checkbox" name="checkbox"  value=Delphi /><label>Delphi</label><br>
# <input type="checkbox" name="checkbox"  value=Django /><label>Django</label><br>
# <input type="checkbox" name="checkbox"  value=Drupal /><label>Drupal</label><br>
# <input type="checkbox" name="checkbox"  value=DynamoDB /><label>DynamoDB</label><br>
# <input type="checkbox" name="checkbox"  value=Elasticsearch /><label>Elasticsearch</label><br>
# <input type="checkbox" name="checkbox"  value=Flask /><label>Flask</label><br>
# <input type="checkbox" name="checkbox"  value=Flow /><label>Flow</label><br>
# <input type="checkbox" name="checkbox"  value=Git /><label>Git</label><br>
# <input type="checkbox" name="checkbox"  value=Go /><label>Go</label><br>
# <input type="checkbox" name="checkbox"  value=Google Cloud Platform /><label>Google Cloud Platform</label><br>
# <input type="checkbox" name="checkbox"  value=Hadoop /><label>Hadoop</label><br>
# <input type="checkbox" name="checkbox"  value=Java /><label>Java</label><br>
# <input type="checkbox" name="checkbox"  value=JavaScript /><label>JavaScript</label><br>
# <input type="checkbox" name="checkbox"  value=Kubernetes /><label>Kubernetes</label><br>
# <input type="checkbox" name="checkbox"  value=LISP /><label>LISP</label><br>
# <input type="checkbox" name="checkbox"  value=MariaDB /><label>MariaDB</label><br>
# <input type="checkbox" name="checkbox"  value=Microsoft Azure /><label>Microsoft Azure</label><br>
# <input type="checkbox" name="checkbox"  value=Node.js /><label>Node.js</label><br>
# <input type="checkbox" name="checkbox"  value=Oracle /><label>Oracle</label><br>
# <input type="checkbox" name="checkbox"  value=PHP /><label>PHP</label><br>
# <input type="checkbox" name="checkbox"  value=Pandas /><label>Pandas</label><br>
# <input type="checkbox" name="checkbox"  value=Perl /><label>Perl</label><br>
# <input type="checkbox" name="checkbox"  value=PowerShell /><label>PowerShell</label><br>
# <input type="checkbox" name="checkbox"  value=Python /><label>Python</label><br>
# <input type="checkbox" name="checkbox"  value=Qt /><label>Qt</label><br>
# <input type="checkbox" name="checkbox"  value=React.js /><label>React.js</label><br>
# <input type="checkbox" name="checkbox"  value=Redis /><label>Redis</label><br>
# <input type="checkbox" name="checkbox"  value=Ruby on Rails /><label>Ruby on Rails</label><br>
# <input type="checkbox" name="checkbox"  value=Rust /><label>Rust</label><br>
# <input type="checkbox" name="checkbox"  value=Scala /><label>Scala</label><br>
# <input type="checkbox" name="checkbox"  value=Swift /><label>Swift</label><br>
# <input type="checkbox" name="checkbox"  value=Terraform /><label>Terraform</label><br>
# <input type="checkbox" name="checkbox"  value=TypeScript /><label>TypeScript</label><br>
# <input type="checkbox" name="checkbox"  value=Unity 3D /><label>Unity 3D</label><br>
# <input type="checkbox" name="checkbox"  value=Vue.js /><label>Vue.js</label><br>
# <input type="checkbox" name="checkbox"  value=Xamarin /><label>Xamarin</label><br>
# <input type="checkbox" name="checkbox"  value=jQuery /><label>jQuery</label><br>
# (base) 
# Dan@DESKTOP-JCINU2U MINGW64 ~/Desktop/Project-3/templates
# $ python html.py
# <input type="checkbox" name="checkbox"  value="AWS" /><label>AWS</label><br>
# <input type="checkbox" name="checkbox"  value="Bash/Shell" /><label>Bash/Shell</label><br>
# <input type="checkbox" name="checkbox"  value="C++" /><label>C++</label><br>
# <input type="checkbox" name="checkbox"  value="COBOL" /><label>COBOL</label><br>
# <input type="checkbox" name="checkbox"  value="Cassandra" /><label>Cassandra</label><br>
# <input type="checkbox" name="checkbox"  value="Clojure" /><label>Clojure</label><br>
# <input type="checkbox" name="checkbox"  value="Crystal" /><label>Crystal</label><br>
# <input type="checkbox" name="checkbox"  value="Delphi" /><label>Delphi</label><br>
# <input type="checkbox" name="checkbox"  value="Django" /><label>Django</label><br>
# <input type="checkbox" name="checkbox"  value="Drupal" /><label>Drupal</label><br>
# <input type="checkbox" name="checkbox"  value="DynamoDB" /><label>DynamoDB</label><br>
# <input type="checkbox" name="checkbox"  value="Elasticsearch" /><label>Elasticsearch</label><br>
# <input type="checkbox" name="checkbox"  value="Flask" /><label>Flask</label><br>
# <input type="checkbox" name="checkbox"  value="Flow" /><label>Flow</label><br>
# <input type="checkbox" name="checkbox"  value="Git" /><label>Git</label><br>
# <input type="checkbox" name="checkbox"  value="Go" /><label>Go</label><br>
# <input type="checkbox" name="checkbox"  value="Google Cloud Platform" /><label>Google Cloud Platform</label><br>
# <input type="checkbox" name="checkbox"  value="Hadoop" /><label>Hadoop</label><br>
# <input type="checkbox" name="checkbox"  value="Java" /><label>Java</label><br>
# <input type="checkbox" name="checkbox"  value="JavaScript" /><label>JavaScript</label><br>
# <input type="checkbox" name="checkbox"  value="Kubernetes" /><label>Kubernetes</label><br>
# <input type="checkbox" name="checkbox"  value="LISP" /><label>LISP</label><br>
# <input type="checkbox" name="checkbox"  value="MariaDB" /><label>MariaDB</label><br>
# <input type="checkbox" name="checkbox"  value="Microsoft Azure" /><label>Microsoft Azure</label><br>
# <input type="checkbox" name="checkbox"  value="Node.js" /><label>Node.js</label><br>
# <input type="checkbox" name="checkbox"  value="Oracle" /><label>Oracle</label><br>
# <input type="checkbox" name="checkbox"  value="PHP" /><label>PHP</label><br>
# <input type="checkbox" name="checkbox"  value="Pandas" /><label>Pandas</label><br>
# <input type="checkbox" name="checkbox"  value="Perl" /><label>Perl</label><br>
# <input type="checkbox" name="checkbox"  value="PowerShell" /><label>PowerShell</label><br>
# <input type="checkbox" name="checkbox"  value="Python" /><label>Python</label><br>
# <input type="checkbox" name="checkbox"  value="Qt" /><label>Qt</label><br>
# <input type="checkbox" name="checkbox"  value="React.js" /><label>React.js</label><br>
# <input type="checkbox" name="checkbox"  value="Redis" /><label>Redis</label><br>
# <input type="checkbox" name="checkbox"  value="Ruby on Rails" /><label>Ruby on Rails</label><br>
# <input type="checkbox" name="checkbox"  value="Rust" /><label>Rust</label><br>
# <input type="checkbox" name="checkbox"  value="Scala" /><label>Scala</label><br>
# <input type="checkbox" name="checkbox"  value="Swift" /><label>Swift</label><br>
# <input type="checkbox" name="checkbox"  value="Terraform" /><label>Terraform</label><br>
# <input type="checkbox" name="checkbox"  value="TypeScript" /><label>TypeScript</label><br>
# <input type="checkbox" name="checkbox"  value="Unity 3D" /><label>Unity 3D</label><br>
# <input type="checkbox" name="checkbox"  value="Vue.js" /><label>Vue.js</label><br>
# <input type="checkbox" name="checkbox"  value="Xamarin" /><label>Xamarin</label><br>
# <input type="checkbox" name="checkbox"  value="jQuery" /><label>jQuery</label><br>

# )