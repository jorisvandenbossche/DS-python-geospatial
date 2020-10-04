# More explicit version defining the x and y axis
argo["buoyancy"].plot.pcolormesh(x="date", y="level", yincrease=False)  # pcolormesh instead of imshow