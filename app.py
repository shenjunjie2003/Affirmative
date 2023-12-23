from affirmative_app import app##, db  # Assuming your package is named affirmative_app

# Optional: Configurations can be set here or imported from a separate file
app.config['DEBUG'] = True  # Enable debug mode for development
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/dbname'
#db.init_app(app)

if __name__ == '__main__':
    app.run()