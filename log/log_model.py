import json
import datetime as df


def log_model(outfile: str, model_name: str, aic:int , bic:int, rmse:int, **kwargs):
    out = {
        "model_name":model_name,
        "aic":aic,
        "bic":bic,
        "rmse":rmse,
        **kwargs
    }
    with open(outfile, mode='a') as file: 
        file.write(json.dumps(out) + '\n')



