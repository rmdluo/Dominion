from ete3 import Tree, TreeNode, faces, AttrFace, TreeStyle

# Layout function code adapted from 
# http://etetoolkit.org/docs/latest/faqs/#how-do-i-visualize-internal-node-names
def my_layout(node):
     if node.name:
          if node.is_leaf():
               # If terminal node, draws its name
               name_face = AttrFace("name")
          else:
               # If internal node, draws label with smaller font size
               name_face = AttrFace("name", fsize=10)
          # Adds the name face to the image at the preferred position
          faces.add_face_to_node(name_face, node, column=0, position="branch-right")

def showTree(newickString):
     ts = TreeStyle()
     # Use my custom layout
     ts.layout_fn = my_layout
     ts.show_scale = None
     ts.show_leaf_name = None
     t = Tree(newickString)
     t.show(tree_style=ts)