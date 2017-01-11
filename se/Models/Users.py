from se.App.Database.Eloquent.Model import Model

# Users class model
class Users(Model):

    # Defining Table Name
    tableName = 'users'

    # Fields you want to show
    fillable = ['id', 'display_name', 'email', 'created_at', 'updated_at']

    #Fields you want to hide
    hidden = ['password']

    # Relation to get the list of all organisations from which one belongs 
    def organisation():
        return Model().belongsToMany('se.Models.Organisation', 'organisation_user', 'user_id', 'organisation_id')