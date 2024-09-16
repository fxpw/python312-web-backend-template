from localization.languages.en import enEN
from localization.languages.ru import ruRU


class __LocalizationClass:
	"""
	Localization class.
	from localization import L
	name = L("test")
	"""

	__currentLocalization: str = "ru"
	__localizationTable: dict[str, dict[str, str]] = {
		"ru": ruRU,
		"en": enEN,
	}

	def GetCurrentLocalization(self) -> str:
		return self.__currentLocalization

	def SetCurrentLocalization(self, newLocalization: str) -> bool:
		if newLocalization in self.__localizationTable:
			self.__currentLocalization = newLocalization
			return True
		return False

	def GetLocString(self, nameOfParam: str, *args: str) -> str:
		strForReturn = nameOfParam
		if self.__currentLocalization in self.__localizationTable:
			if nameOfParam in self.__localizationTable[self.__currentLocalization]:
				strForReturn = str(
					self.__localizationTable[self.__currentLocalization][nameOfParam]
				)
			if len(args) > 0:
				strForReturn = strForReturn.format(*args)
		return strForReturn

	def __call__(self, nameOfParam: str, *args: str) -> str:
		return self.GetLocString(nameOfParam, *args)


L = __LocalizationClass()
