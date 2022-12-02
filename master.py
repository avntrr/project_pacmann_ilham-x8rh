import streamlit as st
import joblib
import numpy as np
import pandas as pd
import yaml
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

params_dir = "/Users/avntrr/Documents/Pacmann/params.yml"

def load_params(param_dir):
    with open(param_dir, "r") as file:
        params = yaml.safe_load(file)
        
    return params

params = load_params(params_dir)


def main():
    with open("/Users/avntrr/Documents/Pacmann/model.pkl", "rb") as file:
        model = joblib.load(file)

        st.title("Prediksi Kualitas Udara di DKI Jakarta")
        st.subheader("Masukkan Nilai Parameter")

        with st.form(key = "kualitas_udara"):
            stasiun = st.selectbox("Nama Stasiun:", ['Pilih Stasiun',
            'DKI1 (Bunderan HI)',
            'DKI2 (Kelapa Gading)',
            'DKI3 (Jagakarsa)',
            'DKI4 (Lubang Buaya)',
            'DKI5 (Kebon Jeruk) Jakarta Barat'])
            pm10 = st.number_input("PM10", min_value=-1, max_value=800, value=0)
            pm25 = st.number_input("PM25", min_value=-1, max_value=400, value=0)
            so2 = st.number_input("SO2", min_value=-1, max_value=500, value=0)
            co = st.number_input("CO", min_value=-1, max_value=100, value=0)
            o3 = st.number_input("O3", min_value=-1, max_value=160, value=0)
            no2 = st.number_input("NO2", min_value=-1, max_value=100, value=0)
    
            submitted = st.form_submit_button("Predict")

            if submitted:
                raw_data = {
            "pm10" : pm10,
            "pm25" : pm25,
            "so2" : so2,
            "co" : co,
            "o3" : o3,
            "no2" : no2,
            "stasiun" : stasiun
                }
    
                df = pd.DataFrame([raw_data])
                ohe_statiun = OneHotEncoder(sparse = False)
                ohe_statiun.fit(np.array(params["range_stasiun"]).reshape(-1, 1))   
                stasiun_features = ohe_statiun.transform(np.array(df.stasiun.to_list()).reshape(-1, 1))
                stasiun_features = pd.DataFrame(stasiun_features, columns = params["range_stasiun"])
                stasiun_features.set_index(df.index, inplace = True)
                test_set = pd.concat([stasiun_features, df], axis = 1)
                test_set.drop(columns = "stasiun", inplace = True)

                prediction = model.predict(test_set)
                st.write("Kualitas Udara:")

                if prediction == 0:
                    st.success("BAIK")
                elif prediction == 1:
                    st.success("TIDAK SEHAT")

if __name__ == "__main__":
    main()

        