import pandas as pd

vids1 = {'https://www.youtube.com/watch?v=Im-pBDFgJcA', 'https://www.youtube.com/watch?v=SuN78CgBjLM', 'https://www.youtube.com/watch?v=AZb1wLIQ1R4', 'https://www.youtube.com/watch?v=og3AyqD5J_g', 'https://www.youtube.com/watch?v=glvYULuaf-k', 'https://www.youtube.com/watch?v=jA2Hyi2VLME', 'https://www.youtube.com/watch?v=pmVgs8wOk5o', 'https://www.youtube.com/watch?v=_caQMy965rs', 'https://www.youtube.com/watch?v=nfveG736mnw', 'https://www.youtube.com/watch?v=mvURH5KhFPk', 'https://www.youtube.com/watch?v=yit1hecSfJE', 'https://www.youtube.com/watch?v=qqETipokc34', 'https://www.youtube.com/watch?v=jq4hI_JbJRo', 'https://www.youtube.com/watch?v=IVJoISiw28c', 'https://www.youtube.com/watch?v=3NfjY7ddHz8', 'https://www.youtube.com/watch?v=Md2eYUuVHkE', 'https://www.youtube.com/watch?v=Bo3M0QXirSY', 'https://www.youtube.com/watch?v=ziWA3MLlook', 'https://www.youtube.com/watch?v=CHxpplpcIWE', 'https://www.youtube.com/watch?v=GDdigOQ4qOY', 'https://www.youtube.com/watch?v=gkRy67OCCpQ', 'https://www.youtube.com/watch?v=2zXbRJty4vc', 'https://www.youtube.com/watch?v=s72FvmjrTw4', 'https://www.youtube.com/watch?v=Mt5x8aR_Xec', 'https://www.youtube.com/watch?v=cSnaA7jkP2w', 'https://www.youtube.com/watch?v=felqbvOnUdc', 'https://www.youtube.com/watch?v=b7OryQDDCsU', 'https://www.youtube.com/watch?v=pFW9zyaVF4U', 'https://www.youtube.com/watch?v=Z7UXVx30If0', 'https://www.youtube.com/watch?v=TxKnV7_WnVE', 'https://www.youtube.com/watch?v=zMTYEWJZWwI', 'https://www.youtube.com/watch?v=m_DRlQUhmB8', 'https://www.youtube.com/watch?v=9dGj5hAi0mE', 'https://www.youtube.com/watch?v=SFkm1rgy-_s', 'https://www.youtube.com/watch?v=UnffRY0btLQ', 'https://www.youtube.com/watch?v=ujyvH3DjisE', 'https://www.youtube.com/watch?v=89YsDUb7SEk', 'https://www.youtube.com/watch?v=n-scVQic3T4', 'https://www.youtube.com/watch?v=4auwnxsEDeI', 'https://www.youtube.com/watch?v=aQVoMfQK-5c', 'https://www.youtube.com/watch?v=vTWpddJiUXI', 'https://www.youtube.com/watch?v=H1PQj54u0As', 'https://www.youtube.com/watch?v=Zvv3v1_DkzE', 'https://www.youtube.com/watch?v=IC5vBKc21X8', 'https://www.youtube.com/watch?v=Yrl2oHO1Ywk', 'https://www.youtube.com/watch?v=I_DXRghJNrI', 'https://www.youtube.com/watch?v=y_buDt2Ne8c', 'https://www.youtube.com/watch?v=KNUJbxhgaeY', 'https://www.youtube.com/watch?v=UIwsc4fOnRY', 'https://www.youtube.com/watch?v=RkQFYT1pmC0', 'https://www.youtube.com/watch?v=kOQG9bQUZCM'}

vids_list = list(vids1)

c1 = 0
df1 = pd.DataFrame({"vids": vids_list,"vid_id":[f"vid_id_{i}" for i in range(len(vids_list))]})
print(df1)

main_data = pd.read_csv("CSVs/main_csv_telesko.csv")
result = pd.merge(df1, main_data, how="left", on=["vid_id", "vid_id"])
result = result.drop(columns="Unnamed:0")
result.to_csv("CSVs/main_csv2_telusko.csv")
print(result)