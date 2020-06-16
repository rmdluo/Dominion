from ete3 import Tree, TreeNode, faces, AttrFace, TreeStyle

# Layout function code adapted from http://etetoolkit.org/docs/latest/faqs/#how-do-i-visualize-internal-node-names
def my_layout(node):
    if node.is_leaf():
         # If terminal node, draws its name
         name_face = AttrFace("name")
    else:
         # If internal node, draws label with smaller font size
         name_face = AttrFace("name", fsize=10)
    # Adds the name face to the image at the preferred position
    faces.add_face_to_node(name_face, node, column=0, position="branch-right")

ts = TreeStyle()
# Use my custom layout
ts.layout_fn = my_layout
ts.show_scale = None
ts.show_leaf_name =None

t = TreeNode("(((((D1.0.0,D1.0.1,D1.0.2)S1.0)B1.0)P1.0)D0.0,((((D1.1.0,D1.1.1)S1.1)B1.1)P1.1)D0.1,((((D1.2.0,D1.2.1,D1.2.2,D1.2.3)S1.2)B1.2)P1.2)D0.2)S0;",format=8)
t.show(tree_style=ts)
ancestor = t.get_common_ancestor("D1.2.0","D1.0.1")
print(ancestor)