import wx
import wx.stc as stc

def syntax(self):
	if self.filepath=='untitled':
		pass
	elif self.fileext=='.cfg':
		self.control.SetLexer(stc.STC_LEX_PYTHON)
		self.control.StyleSetSpec(stc.STC_P_COMMENTLINE, "fore:#616161,back:#212121,"+self.cstyle+",face:"+self.cfont+",size:"+self.cfontsize)
		self.control.StyleSetSpec(stc.STC_P_OPERATOR, "fore:white,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_P_IDENTIFIER, "fore:#80DEEA,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_P_NUMBER, "fore:#7E57C2,back:#212121,face:"+self.font+",size:"+self.fontsize)
	elif self.fileext=='.css':
		self.control.SetLexer(stc.STC_LEX_CSS)
		self.control.StyleSetSpec(stc.STC_CSS_DEFAULT, "fore:white,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_CSS_COMMENT, "fore:#616161,back:#212121,"+self.cstyle+",face:"+self.cfont+",size:"+self.cfontsize)
		self.control.StyleSetSpec(stc.STC_CSS_ID, "fore:#D81B60,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_CSS_TAG, "fore:#9CCC65,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_CSS_CLASS, "fore:#D81B60,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_CSS_VALUE, "fore:#7E57C2,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_CSS_OPERATOR, "fore:#ffffff,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_CSS_SINGLESTRING, "fore:#FDD835,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_CSS_DOUBLESTRING, "fore:#FDD835,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_CSS_IDENTIFIER, "fore:#80DEEA,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_CSS_IDENTIFIER2, "fore:#80DEEA,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_CSS_UNKNOWN_IDENTIFIER, "fore:#80DEEA,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_CSS_PSEUDOCLASS, "fore:white,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_CSS_UNKNOWN_PSEUDOCLASS, "fore:white,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_CSS_ATTRIBUTE, "fore:white,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_CSS_DIRECTIVE, "fore:white,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_CSS_IMPORTANT, "fore:white,back:#212121,face:"+self.font+",size:"+self.fontsize)
	elif self.fileext=='.xml':
		self.control.SetLexer(stc.STC_LEX_XML)
		self.control.StyleSetSpec(stc.STC_H_DEFAULT, "fore:#ffffff,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_NUMBER, "fore:#7E57C2,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_COMMENT, "fore:#616161,back:#212121,"+self.cstyle+",face:"+self.cfont+",size:"+self.cfontsize)
		self.control.StyleSetSpec(stc.STC_H_SINGLESTRING, "fore:#FDD835,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_DOUBLESTRING, "fore:#FDD835,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_XMLSTART, "fore:#D81B60,back:#212121,italic,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_XMLEND, "fore:#D81B60,back:#212121,italic,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_TAG, "fore:#D81B60,back:#212121,italic,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_TAGEND, "fore:#D81B60,back:#212121,italic,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_TAGUNKNOWN, "fore:RED,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_ATTRIBUTE, "fore:#9CCC65,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_ATTRIBUTEUNKNOWN, "fore:RED,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_OTHER, "fore:#ffffff,back:#212121,face:"+self.font+",size:"+self.fontsize)
	elif self.fileext=='.html':
		self.control.SetLexer(stc.STC_LEX_HTML)
		self.control.StyleSetSpec(stc.STC_H_DEFAULT, "fore:#ffffff,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_TAG, "fore:#D81B60,back:#212121,italic,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_TAGEND, "fore:#D81B60,back:#212121,italic,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_TAGUNKNOWN, "fore:RED,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_NUMBER, "fore:#7E57C2,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_COMMENT, "fore:#616161,back:#212121,"+self.cstyle+",face:"+self.cfont+",size:"+self.cfontsize)
		self.control.StyleSetSpec(stc.STC_H_SINGLESTRING, "fore:#FDD835,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_DOUBLESTRING, "fore:#FDD835,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_ATTRIBUTE, "fore:#9CCC65,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_ATTRIBUTEUNKNOWN, "fore:RED,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_OTHER, "fore:#FFFFFF,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_SCRIPT, "fore:RED,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_QUESTION, "fore:RED,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_VALUE, "fore:RED,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_CDATA, "fore:RED,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_ASPAT, "fore:RED,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_SGML_DEFAULT, "fore:#D81B60,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_H_SGML_ERROR, "fore:#D81B60,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_HJ_DEFAULT, "fore:RED,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_HJ_NUMBER, "fore:#7E57C2,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_HJ_SINGLESTRING, "fore:#FDD835,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_HJ_DOUBLESTRING, "fore:#FDD835,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_HJ_WORD, "fore:#9CCC65,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_HJ_SYMBOLS, "fore:#D81B60,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_HJ_COMMENT, "fore:#616161,back:#212121,"+self.cstyle+",face:"+self.cfont+",size:"+self.cfontsize)
		self.control.StyleSetSpec(stc.STC_HJ_COMMENTLINE, "fore:#616161,back:#212121,"+self.cstyle+",face:"+self.cfont+",size:"+self.cfontsize)
	elif self.fileext=='.py':
		self.control.SetLexer(stc.STC_LEX_PYTHON)
		self.control.StyleSetSpec(stc.STC_P_DEFAULT, "fore:#FFFFFF,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_P_COMMENTLINE, "fore:#616161,back:#212121,"+self.cstyle+",face:"+self.cfont+",size:"+self.cfontsize)
		self.control.StyleSetSpec(stc.STC_P_NUMBER, "fore:#7E57C2,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_P_STRING, "fore:#FDD835,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_P_CHARACTER, "fore:#FDD835,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_P_WORD, "fore:RED,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_P_TRIPLE, "fore:#FDD835,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_P_TRIPLEDOUBLE, "fore:#FDD835,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_P_CLASSNAME, "fore:#D81B60,back:#212121,bold,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_P_DEFNAME, "fore:#D81B60,back:#212121,bold,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_P_OPERATOR, "fore:white,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_P_IDENTIFIER, "fore:#9CCC65,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_P_COMMENTBLOCK, "fore:#616161,back:#212121,"+self.cstyle+",face:"+self.cfont+",size:"+self.cfontsize)
		self.control.StyleSetSpec(stc.STC_P_STRINGEOL, "fore:red,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_P_WORD2, "fore:red,back:#212121,face:"+self.font+",size:"+self.fontsize)
		self.control.StyleSetSpec(stc.STC_P_DECORATOR, "fore:red,back:#212121,face:"+self.font+",size:"+self.fontsize)
	else:
		pass
