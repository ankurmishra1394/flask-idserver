from se.App.Database.Eloquent.Model import Model

# Apps class model
class Apps(Model):

    # Defining Table Name
    tableName = 'apps'

    # Fields you want to show
    fillable = ['id', 'name', 'url', 'description', 'logo', 'created_by', 'created_at', 'updated_at']

    def organisation(self.tableName):
        return Model().hasMany('se.Models.Organisation', 'organisation_apps', 'app_id')
