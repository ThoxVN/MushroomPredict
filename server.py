from flask import Flask, render_template, request
import pandas as pd
import ipywidgets as widgets
from sklearn.preprocessing import OneHotEncoder
import pickle
from sklearn.decomposition import PCA


app = Flask(__name__)

knn = pickle.load(open('knn.pkl', 'rb'))

pca1 = PCA(n_components = 8)
pca1.explained_variance_ratio_

attributes = [
    '1. cap-shape: bell=0,conical=1,convex=5,flat=2,knobbed=3,sunken=4',
    '2. cap-surface: fibrous=0,grooves=1,scaly=3,smooth=2',
    '3. cap-color: brown=4,buff=0,cinnamon=1,gray=3,green=6,pink=5,purple=7,red=2,white=8,yellow=9',
    '4. bruises?: bruises=1,no=0',
    '5. odor: almond=0,anise=3,creosote=1,fishy=8,foul=2,musty=4,none=5,pungent=6,spicy=7',
    '6. gill-attachment: attached=0,descending=2,free=1,notched=3',
    '7. gill-spacing: close=0,crowded=1,distant=2',
    '8. gill-size: broad=0,narrow=1',
    '9. gill-color: black=4,brown=5,buff=0,chocolate=3,gray=2,green=8,orange=6,pink=7,purple=9,red=1,white=10,yellow=11',
    '10. stalk-shape: enlarging=0,tapering=1',
    '11. stalk-root: bulbous=1,club=2,cup=5,equal=3,rhizomorphs=6,rooted=4,missing=0',
    '12. stalk-surface-above-ring: fibrous=0,scaly=3,silky=1,smooth=2',
    '13. stalk-surface-below-ring: fibrous=0,scaly=3,silky=1,smooth=2',
    '14. stalk-color-above-ring: brown=4,buff=0,cinnamon=1,gray=3,orange=5,pink=6,red=2,white=7,yellow=8',
    '15. stalk-color-below-ring: brown=4,buff=0,cinnamon=1,gray=3,orange=5,pink=6,red=2,white=7,yellow=8',
    '16. veil-type: partial=0,universal=1',
    '17. veil-color: brown=0,orange=1,white=2,yellow=3',
    '18. ring-number: none=0,one=1,two=2',
    '19. ring-type: cobwebby=5,evanescent=0,flaring=1,large=2,none=3,pendant=4,sheathing=6,zone=7',
    '20. spore-print-color: black=2,brown=3,buff=0,chocolate=1,green=5,orange=4,purple=6,white=7,yellow=8',
    '21. population: abundant=0,clustered=1,numerous=2,scattered=3,several=4,solitary=5',
    '22. habitat: grasses=1,leaves=2,meadows=3,paths=4,urban=5,waste=6,woods=0'
]

options = {
    'cap-shape': [0,1,2,3,4,5],
    'cap-surface': [0,1,2,3],
    'cap-color': [0,1,2,3,4,5,6,7,8,9],
    'bruises?': [0,1],
    'odor': [0,1,2,3,4,5,6,7,8],
    'gill-attachment': [0,1,2,3],
    'gill-spacing': [0,1,2],
    'gill-size': [0,1],
    'gill-color': [0,1,2,3,4,5,6,7,8,9,10,11],
    'stalk-shape': [0,1],
    'stalk-root': [0,1,2,3,4,5,6],
    'stalk-surface-above-ring': [0,1,2,3],
    'stalk-surface-below-ring': [0,1,2,3],
    'stalk-color-above-ring': [0,1,2,3,4,5,6,7,8],
    'stalk-color-below-ring': [0,1,2,3,4,5,6,7,8],
    'veil-type': [0,1],
    'veil-color': [0,1,2,3],
    'ring-number': [0,1,2],
    'ring-type': [0,1,2,3,4,5,6,7],
    'spore-print-color': [0,1,2,3,4,5,6,7,8],
    'population': [0,1,2,3,4,5],
    'habitat': [0,1,2,3,4,5,6]
}

dropdowns = {name: widgets.Dropdown(options=opts, description=name.replace('-', ' ').title() + ':') for name, opts in options.items()}

encoder = OneHotEncoder()

@app.route('/')
def index():
    return render_template('index.html', attributes=attributes, dropdowns=dropdowns)

from flask import request, jsonify

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = {name: dropdown.value for name, dropdown in dropdowns.items()}
        df = pd.DataFrame(data, index=[0])
        transformed_data = pca1.transform(df)
        predictY = knn.predict(transformed_data)   
        
        if predictY == 1:
            return jsonify({'result': 'Poisonous'})
        else:
            return jsonify({'result': 'Edible'})      
        
    else:
        return render_template('index2.html', dropdowns=dropdowns)
if __name__ == '__main__':
  app.run(port=5000,debug=True)

