# -*- coding: gb2312 -*-
#
import xlsxtool
def funcInt(mapDict, dctData, chilidDict, data):
	"""
	����int����
	"""
	try:
		v = eval(data)
	except:
		return 0

	if type(v) != int:
		return 0

	return v

def funcFloat(mapDict, dctData, chilidDict, data):
	"""
	����float����
	"""
	if data is None or (type(data) == str and len(data) == 0):
		return 0.0

	return float(data)

def funcStr(mapDict, dctData, chilidDict, data):
	"""
	�����ַ�������
	"""
	if data is None:
		return ""

	if type(data) == str:
		return data
	elif type(data) == unicode:
		return data.encode("utf-8")
	else:
		return str(data)

def funcEval(mapDict, dctData, chilidDict, data):
	"""
	����eval����
	"""
	if data is None or (type(data) == str and len(data) == 0):
		return ""
	return eval(data)

def funcTupleInt(mapDict, dctData, chilidDict, data):
	"""
	����tuple����
	"""
	if data is None or (type(data) == str and len(data) == 0):
		return ()

	data = str(data)

	return tuple([int(e) for e in data.split(",") if len(e) > 0])

def funcDict(mapDict, dctData, chilidDict, data):
	"""
	����dict����
	"xx:1'2'3;fff:2'3'4"
	"""
	if data is None or (type(data) == str and len(data) == 0):
		return ''
	
	data = str(data)
	dict1 = {}
	for item in data.split(';'):
		if item != '':
			 e = item.split(':')
			 if len(e) == 1:
			 	 dict1[int(e[0])] = ()
			 elif len(e) == 2:
			 	 dict1[int(e[0])] = tuple([index for index in e[1].split('`') if index != ''])

	return dict1

def funcTupleStr(mapDict, dctData, chilidDict, data):
	"""
	����tuple����
	"""
	if data is None or (type(data) == str and len(data) == 0):
		return ()

	data = str(data)
	return tuple([e for e in data.split(",") if len(e) > 0])

def funcTupleEval(mapDict, dctData, chilidDict, data):
	"""
	����tuple����
	"""
	if data is None or (type(data) == str and len(data) == 0):
		return ()

	data = str(data)
	return tuple([eval(e) for e in data.split(",") if len(e) > 0])

def funcTupleEvalMD(mapDict, dctData, chilidDict, data):
	"""
	����tuple���� ʹ�ô��Ա�
	"""
	if data is None or (type(data) == str and len(data) == 0):
		return ()
	
	data = str(data)
	try:
		return tuple([eval(mapDict[e.decode("gb2312")]) for e in data.split(",") if len(e) > 0])
	except Exception, errstr:
		print "�����з�������:%s" % errstr
		return ()
	
def funcTupleEval1(mapDict, dctData, chilidDict, data):
	"""
	����tuple����
	1'100/2'100/3'54
	"""
	if data is None or (type(data) == str and len(data) == 0):
		return ()

	data = str(data)
	ret = []
	for e in data.split("/"):
		try:
			i, v = e.split("'")
		except Exception, errstr:
			print "�����з�������:%s" % errstr
			continue
		ret.append((eval(i), eval(v)))
	return tuple(ret)
	
def funcBool(mapDict, dctData, chilidDict, data):
	"""
	���ز���ֵ
	"""
	if data is None or (type(data) == str and len(data) == 0):
		return False
	return int(data) > 0

def funcNotBool(mapDict, dctData, chilidDict, data):
	"""
	����ȡ���Ĳ���ֵ
	"""
	return not funcBool(mapDict, dctData, chilidDict, data)

def funcNull(mapDict, dctData, chilidDict, data):
	"""
	ʲôҲ���� ֱ�ӷ���
	"""
	return data

def funcZipFloat(mapDict, dctData, chilidDict, data):
	"""
	����float����
	"""
	if data is None or (type(data) == str and len(data) == 0):
		return 0

	return int(float(data) * 10000)

def funcUNZipFloat(mapDict, dctData, chilidDict, data):
	"""
	����float����
	"""
	if data is None or (type(data) == str and len(data) == 0):
		return 0.0

	return int(data) / 10000.0
	