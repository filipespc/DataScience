import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("data/CRDC2013_14.csv",encoding="Latin-1")
    
    data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]
    all_HI = data["SCH_ENR_HI_M"].sum() + data["SCH_ENR_HI_F"].sum()
    all_AM = data["SCH_ENR_AM_M"].sum() + data["SCH_ENR_AM_F"].sum()
    all_AS = data["SCH_ENR_AS_M"].sum() + data["SCH_ENR_AS_F"].sum()
    all_HP = data["SCH_ENR_HP_M"].sum() + data["SCH_ENR_HP_F"].sum()    
    all_BL = data["SCH_ENR_BL_M"].sum() + data["SCH_ENR_BL_F"].sum()
    all_WH = data["SCH_ENR_WH_M"].sum() + data["SCH_ENR_WH_F"].sum()
    all_TR = data["SCH_ENR_TR_M"].sum() + data["SCH_ENR_TR_F"].sum()
    
    all_M =  data["SCH_ENR_HI_M"].sum() + data["SCH_ENR_AM_M"].sum() + data["SCH_ENR_AS_M"].sum() + data["SCH_ENR_HP_M"].sum() + data["SCH_ENR_BL_M"].sum() + data["SCH_ENR_WH_M"].sum() + data["SCH_ENR_TR_M"].sum()
    all_F = data["SCH_ENR_HI_F"].sum() + data["SCH_ENR_AM_F"].sum() + data["SCH_ENR_AS_F"].sum() + data["SCH_ENR_HP_F"].sum() + data["SCH_ENR_BL_F"].sum() + data["SCH_ENR_WH_F"].sum() + data["SCH_ENR_TR_F"].sum()
    
    all_enrollment = data["total_enrollment"].sum()
    
    print("Hispanic proportion: ",all_HI/all_enrollment)
    print("American Indian proportion: ",all_AM/all_enrollment)
    print("Asian proportion: ",all_AS/all_enrollment)
    print("Hawaiian or Pacific Islander proportion: ",all_HP/all_enrollment)
    print("Black proportion: ",all_BL/all_enrollment)
    print("White proportion: ",all_WH/all_enrollment)
    print("Tow or more races proportion: ",all_TR/all_enrollment)
    
    print("Male proportion: ",all_M/all_enrollment)
    print("Femael proportion: ",all_F/all_enrollment)