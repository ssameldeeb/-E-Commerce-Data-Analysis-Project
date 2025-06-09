import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import os


data = pd.read_csv("online_store_sales_4000_rows.csv")

print(data.shape)
print(data.columns.values)
print(data.dtypes)
print(data.dtypes.value_counts())
print(data.isna().sum())
print(data.isna().sum().sum())

print(data.head(5))


data = data.drop(["OrderID","Brand"], axis=1)
print(data.head(5))

data["OrderDate"] = pd.to_datetime(data["OrderDate"])
print(data["OrderDate"].dtype)

data["Year"] = data["OrderDate"].dt.year
data["Month"] = data["OrderDate"].dt.month
data["Day"] = data["OrderDate"].dt.day
data = data.drop("OrderDate", axis=1)
print(data.head(5))

print(data.groupby("ProductCategory")["Quantity","FinalPrice"].sum().sort_values("Quantity"))

os.system("md save")
cou = ["Year","Month","Day","ProductCategory","CustomerLocation","IsPromotion"]
for x in cou:
    print(x.upper())
    plt.figure(figsize=(10,5))
    plt.tight_layout()
    plt.title("Count_" + x)
    sns.countplot(data[x])
    # plt.savefig("save/" + x + '.png')



dis = ["Quantity", "Discount"]
for x in dis:
    print(x.upper())
    plt.figure(figsize=(10,5))
    plt.tight_layout()
    plt.title("Distiny_" + x)
    # plt.savefig("save/" + x + '.png')
    
    
xx = data.groupby("ProductCategory")["FinalPrice"].sum().head().index
yy = data.groupby("ProductCategory")["FinalPrice"].sum().head().values
print(xx)
print(yy)
plt.figure(figsize=(10,5))
plt.tight_layout()
plt.title("pie_for_ProductCategory")
plt.pie(yy, labels= xx, shadow=True)
plt.legend(loc="lower right")
plt.savefig("save/" + "ProductCategory" + '.png')
plt.show()

xx = data.groupby("CustomerLocation")["FinalPrice"].sum().head().index
yy = data.groupby("CustomerLocation")["FinalPrice"].sum().head().values
print(xx)
print(yy)
plt.figure(figsize=(10,5))
plt.tight_layout()
plt.title("pie_for_CustomerLocation")
plt.pie(yy, labels= xx, shadow=True)
plt.legend(loc="lower right")
plt.savefig("save/" + "CustomerLocation" + '.png')
plt.show()