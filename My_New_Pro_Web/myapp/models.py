from sqlalchemy import ForeignKey
from myapp import db 

class Company(db.Model):
    __tablename__='Company'
    Sno=db.Column(db.Integer(),primary_key=True)
    EmpName=db.Column(db.String(20))
    EmpSalary=db.Column(db.Float())
    EmpId=db.Column(db.Integer())
    password=db.Column(db.String(8))

    def __repr__(self):
        return  "<EMPLOYEE DETAILS: {0},{1},{2},{3}>".format(self.Sno,self.EmpName,self.EmpSalary,self.EmpId,self.password)
    
class EmpTechArea(db.Model):
    __tablename__='EmpTechArea'
    Sno=db.Column(db.Integer(),primary_key=True)
    EmpName=db.Column(db.String(20),ForeignKey("Company.EmpName"))
    TechArea=db.Column(db.String(15))
    EmpId=db.Column(db.Integer(),ForeignKey("Company.EmpId"))
    
    def __repr__(self):
        return  "<EMPLOYEE DETAILS: {0},{1},{2}>".format(self.Sno,self.TechArea,self.EmpId)
    
# db.drop_all()
# db.create_all()

# db.session.add(Company(EmpName="Rahul",EmpSalary=23156.5,EmpId=000000))
# db.session.add(Company(EmpName="Ravi",EmpSalary=33156.5,EmpId=1111111))


# db.session.add(EmpTechArea(EmpName="Rahul",TechArea='hellobu',EmpId=15250))
# db.session.add(EmpTechArea(EmpName="Ravi",TechArea="GFS",EmpId=1111111))
# db.session.commit()



    

    
