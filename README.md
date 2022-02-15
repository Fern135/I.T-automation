# I.T-automation
using python to automate some boring i.t tasks like using ccleaner and malwarebytes. 


<!-- macOS/Linux You may need to run sudo apt-get install python3-venv first -->
python3 -m venv venv


<!-- Windows You can also use py -3 -m venv .venv -->
python -m venv venv

<!-- windows activate venv -->
.\venv\Scripts\activate

<!-- if using mac or linux mac / linux activate venv -->
source venv/bin/activate

<!-- install all the requirements -->
pip install -r requirements.txt

<!-- anything bellowe here it's optional -->
<!-- update all packages -->
pip-review --auto

<!-- windows -->
python -m pip install --upgrade pip

<!-- if using mac or linux mac / linux  -->
python3 -m pip install --upgrade pip