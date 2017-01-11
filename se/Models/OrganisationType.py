from se.App.Database.Eloquent.Model import Model

# Organisation class model
class OrganisationType(Model):

    # Defining Table Name
    tableName = 'organisation_type'

    # Fields you want to show
    fillable = ['id', 'name', 'description', 'created_by', 'created_at', 'updated_at']

    def organisation(self.tableName):
        return Model().hasMany('se.Models.Organisation', 'organisation_orgaisation_type', 'organisation_type_id')

    def type(self.tableName):
        return Model().hasMany('se.Models.Type', 'organisation_organisation_type', 'organisation_id')

