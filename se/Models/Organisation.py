from se.App.Database.Eloquent.Model import Model

# Organisation class model
class Organisation(Model):

    # Defining Table Name
    tableName = 'organisation'

    # Fields you want to show
    fillable = ['id', 'name', 'url', 'description', 'logo', 'created_by', 'created_at', 'updated_at']

    # Relation to get the list of all organisations from which one belongs 
    def user(self.tableName):
        return Model().belongsToMany('se.Models.User', 'organisation_user', 'organisation_id', 'user_id')

    def apps(self.tableName):
        return Model().hasMany('se.Models.Apps', 'organisation_apps', 'organisation_id')

    def type(self.tableName):
        return Model().hasMany('se.Models.Type', 'organisation_organisation_type', 'organisation_id')

