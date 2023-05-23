import * as XLSX from 'xlsx';

export async function sheetFileToJson<T>(file: File) {
	const arrayBuffer = await file.arrayBuffer();
	const wb = XLSX.read(arrayBuffer);
	const wsname = wb.SheetNames[0];
	const ws = wb.Sheets[wsname];
	return XLSX.utils.sheet_to_json<T>(ws);
}
