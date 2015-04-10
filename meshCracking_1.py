
#cracking algorithm
import rhinoscriptsyntax as rs
import Rhino
import scriptcontext

def crackpolygon(meshes, count):
    tempMeshes = meshes
    newMeshes = []
    if count == 0:
        return 1
    else:
        for mesh in tempMeshes:
            
            if rs.MeshVertexCount(mesh) != 3 and rs.MeshVertexCount(mesh)!= 4:
                countV = rs.MeshVertexCount(mesh)
                print "mesh has too many vertices"
            else:
                #print "Cool"
                centroid = rs.MeshAreaCentroid(mesh)
                normals = rs.MeshFaceNormals(mesh)
                centroid = rs.PointAdd(centroid, normals[0]*count*.7)
                vertices = rs.MeshVertices(mesh)
                for i in range(1,len(vertices)):
                    newVertices = []
                    newVertices.append(vertices[i])
                    newVertices.append(centroid)
                    newVertices.append(vertices[i-1])
                    newFaces = [[0,1,2]]
                    newMesh = rs.AddMesh(newVertices, newFaces)
                    newMeshes.append(newMesh)
                    
                newVertices = []
                newVertices.append(vertices[0])
                newVertices.append(centroid)
                newVertices.append(vertices[len(vertices)-1])
                newFaces = [[0,1,2]]
                newMesh = rs.AddMesh(newVertices, newFaces)
                newMeshes.append(newMesh)
                
        count = count - 1
        return crackpolygon(newMeshes, count)


def main():
    count = rs.GetInteger("How many iterations would you like to do?", 3)
    mesh = rs.GetObject("pick a mesh to crack",32)
    polygons = []
    polygons.append(mesh)
    crackpolygon(polygons, count)
    


if __name__=="__main__":
    main()