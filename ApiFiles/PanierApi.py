from flask import Blueprint,request,jsonify
import DatabaseFiles.connection as connection

panier_api = Blueprint('panier_api',__name__)


@panier_api.route('/panier/<string:mail>',methods=['GET'])
def beer_by_user(mail) :
    conn = connection.db_connection()
    cursor= conn.cursor()
    if request.method=='GET' :
        cursor.execute("SELECT * FROM beer WHERE id in (SELECT beer_id from beerlist where user_id in (SELECT id FROM user WHERE mail =?))",(str(mail),))
        beers = [
            dict(id=row[0],name = row[1], percentageAlcohol=row[2], category=row[3],stock=row[4],image=row[5])
            for row in cursor.fetchall()
        ]
        cursor.close()
        conn.close()
        return jsonify(beers)

@panier_api.route('/panier',methods=['POST','DELETE'])
def favorite():
    conn = connection.db_connection()
    cursor= conn.cursor()
    if request.method=='POST' :
        data = request.get_json()
        beer_id=data['beer_id']
        user_id = data['user_id']
        sqllist = """INSERT INTO beerlist (user_id,beer_id) VALUES (?,?) """
        cursor.execute(sqllist,(user_id,beer_id))
        conn.commit()
        cursor.close()
        conn.close()
        return f"Beer {beer_id} add to your favlist"
    if request.method=='DELETE' :
        data = request.get_json()
        beer_id=data['beer_id']
        user_id = data['user_id']
        sqllist = """DELETE FROM beerlist where user_id = ? and beer_id=? """
        cursor.execute(sqllist,(user_id,beer_id))
        conn.commit()
        cursor.close()
        conn.close()
        return f"Beer {beer_id} remove from your favlist"