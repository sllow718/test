from django.db import models
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse


class addresources(models.Model):
    Name_of_Resource = models.CharField(max_length = 500)
    HS_Code = models.IntegerField()


    def __str__(self):
        return self.Name_of_Resource

#CASCADE(collector, field, sub_objs, using) maybe useful for selective delete
class addmatchingresources(models.Model):
    add_resources=models.ForeignKey(addresources, on_delete=models.CASCADE)
    Name_of_Matching_Resource = models.CharField(max_length = 500)
    Matching_HS_Code = models.IntegerField()
    Check_if_matches_interchangeable = models.BooleanField(default=False)
    Extraction_rate = models.DecimalField(max_digits=6,decimal_places=3)
    Source = models.CharField(max_length = 500)

    def __str__(self):
        return self.Name_of_Matching_Resource


class editresources(models.Model):
    Name_of_Resource = models.CharField(max_length = 500)
    HS_Code = models.IntegerField()

    def __str__(self):
        return self.Name_of_Resource


class Technologies(models.Model):
    add_resources=models.ForeignKey(addresources, on_delete=models.CASCADE)
    add_matchingresources=models.ForeignKey(addmatchingresources, on_delete=models.CASCADE)
    Method = models.TextField()
    Process = models.TextField()

    def __str__(self):
        return self.Method

#DFS onwards
def generate_adjacency_map():
    all_resources = addresources.objects.all()
    adjacency_map = {}
    for a in all_resources:
        matches = a.addmatchingresources_set.all()
        child_array = []
        if matches:
            for child in matches:
                child_array += [str(child.Matching_HS_Code)]
            adjacency_map[str(a.HS_Code)] = child_array
        else:
            adjacency_map[str(a.HS_Code)] = child_array
    return adjacency_map


def traverse(adjacency_map, starting_node, final_path):
    do_traverse(adjacency_map, starting_node, [starting_node], final_path)
    return final_path

def do_traverse(adjacency_map, current_node, current_path, final_path):
    children = adjacency_map[current_node]
    untraversed_children = []
    for child in children:
        if child not in current_path:
            untraversed_children += [child]

    if len(untraversed_children) > 0:
        for child in untraversed_children:
            do_traverse(adjacency_map, child, current_path + ["->"] + [child], final_path)
    else:
        final_path += [current_path]
