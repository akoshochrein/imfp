
def get_or_none(model, id):
    return model.objects.filter(id=id).first()
