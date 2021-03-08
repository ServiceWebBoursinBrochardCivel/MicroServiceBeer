from flask import Blueprint,request,jsonify
import Database.connection as connection
from main import verifyToken

panier_api = Blueprint('panier_api',__name__)


@panier_api.route('/panier/<int:user_id>',methods=['GET'])
def beer_by_user(user_id) :
    conn = connection.db_connection()
    cursor= conn.cursor()
    if request.method=='GET' :
        cursor.execute("SELECT beer_id,quantite from beerlist where user_id = ?",(int(user_id),))
        beers = [
            dict(beer_id = row[0],quantite=row[1])
            for row in cursor.fetchall()
        ]
        cursor.close()
        conn.close()
        return jsonify(beers)
    
@panier_api.route('/panier/<int:beer_id>/<int:user_id>',methods=['DELETE','PUT'])
def changePanier(beer_id,user_id) :
    conn = connection.db_connection()
    cursor= conn.cursor()
    if request.method=='DELETE' :
        sqllist = """DELETE FROM beerlist where user_id = ? and beer_id=? """
        cursor.execute(sqllist,(int(user_id),int(beer_id)))
        conn.commit()
        cursor.close()
        conn.close()
        return f"Beer {int(beer_id)} remove from your favlist"
    if request.method=='PUT':
        sql = """UPDATE beerlist
                SET quantite = ?                    
                WHERE user_id=? and beer_id=? """
        data = request.get_json()
        quantite = data["quantite"]
        updated_beer_quantite = {
            'user_id' : int(user_id),
            'beer_id' : int(beer_id),
            'quantite' : quantite,
        }
        cursor.execute(sql,(quantite,int(user_id),int(beer_id)))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify(updated_beer_quantite)

@panier_api.route('/panier',methods=['POST'])
def panier():
    conn = connection.db_connection()
    cursor= conn.cursor()
    if request.method=='POST' :
        data = request.get_json()
        beer_id=data['beer_id']
        user_id = data['user_id']
        quantite = data['quantite']
        sqllist = """INSERT INTO beerlist (user_id,beer_id,quantite) VALUES (?,?,?) """
        cursor.execute(sqllist,(user_id,beer_id,quantite))
        conn.commit()
        cursor.close()
        conn.close()
        return f"Beer {beer_id} add to your favlist"