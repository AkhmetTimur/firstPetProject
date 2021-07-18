import os
import matplotlib
matplotlib.use('Agg') # to use plt with flask
import matplotlib.pyplot as plt
from flask import current_app
from flask_login import current_user



def plot(user_id, userdate,userweight):
    #clean previous plot
    plt.clf()
    #to create a graphic
    left = userdate
    height = userweight
    plt.plot(left,height,linewidth=2, markersize=5, marker='o')
    plt.ylabel('weight')
    # to turn off labels
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    prev_picture = os.path.join(current_app.root_path,'static','images', str(current_user.id),'.png')
    if os.path.exists(prev_picture):
            os.remove(prev_picture)
    picture=str(user_id)+'.png'
    path = os.path.join(current_app.root_path,'static','images', picture)
    plt.savefig(path)
    return picture