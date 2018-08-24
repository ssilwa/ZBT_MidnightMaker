from pymongo import MongoClient


def setup_client(uri = "mongodb://<dbuser>:<dbpassword>@ds151951.mlab.com:51951/heroku_1jkknfgn"):
	return MongoClient(uri)



if __name__ == '__main__':
	c = setup_client()
	print(c.zebes.distinct( "kerberos" ))
